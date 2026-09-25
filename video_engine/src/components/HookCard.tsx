import React from "react";
import { spring, useCurrentFrame, useVideoConfig } from "remotion";

export const HookCard: React.FC<{
  hookText: string;
  category?: string;
  icon?: string;
}> = ({ hookText, category = "TDAH EN ADULTOS", icon = "🧠" }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const entrance = spring({
    frame,
    fps,
    config: {
      damping: 14,
      stiffness: 120,
      mass: 0.8,
    },
  });

  const scale = entrance;
  const opacity = Math.min(1, entrance * 1.2);

  // Subtle floating icon bounce
  const iconBounce = Math.sin(frame / 12) * 8;

  return (
    <div
      style={{
        position: "absolute",
        top: 240,
        left: 60,
        width: 960,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        textAlign: "center",
        transform: `scale(${scale})`,
        opacity,
        zIndex: 40,
      }}
    >
      {/* Category Pill */}
      <div
        style={{
          padding: "10px 24px",
          borderRadius: 24,
          backgroundColor: "rgba(233, 128, 110, 0.2)",
          border: "1px solid rgba(233, 128, 110, 0.5)",
          color: "#E9806E",
          fontFamily: "system-ui, -apple-system, sans-serif",
          fontWeight: 800,
          fontSize: 22,
          letterSpacing: "0.08em",
          marginBottom: 24,
          textTransform: "uppercase",
        }}
      >
        {category}
      </div>

      {/* Floating Animated Icon */}
      <div
        style={{
          fontSize: 100,
          transform: `translateY(${iconBounce}px)`,
          filter: "drop-shadow(0 14px 28px rgba(0, 0, 0, 0.6))",
          marginBottom: 20,
        }}
      >
        {icon}
      </div>

      {/* Big Impact Hook Title */}
      <div
        style={{
          fontFamily: "system-ui, -apple-system, sans-serif",
          fontWeight: 900,
          fontSize: 54,
          lineHeight: 1.18,
          color: "#FFFFFF",
          textShadow: "0 8px 32px rgba(0, 0, 0, 0.8)",
          padding: "0 20px",
        }}
      >
        {hookText}
      </div>
    </div>
  );
};
