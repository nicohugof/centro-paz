import React from "react";
import { spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ShortScene } from "../types";

export const PointCard: React.FC<{
  scene: ShortScene;
  relativeFrame: number;
}> = ({ scene, relativeFrame }) => {
  const { fps } = useVideoConfig();

  const entrance = spring({
    frame: relativeFrame,
    fps,
    config: {
      damping: 15,
      stiffness: 140,
      mass: 0.7,
    },
  });

  const translateY = (1 - entrance) * 50;
  const opacity = Math.min(1, entrance * 1.3);

  return (
    <div
      style={{
        position: "absolute",
        top: 260,
        left: 60,
        width: 960,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        textAlign: "center",
        transform: `translateY(${translateY}px) scale(${entrance})`,
        opacity,
        zIndex: 40,
      }}
    >
      {/* Icon */}
      {scene.icon && (
        <div
          style={{
            fontSize: 88,
            filter: "drop-shadow(0 12px 24px rgba(0, 0, 0, 0.5))",
            marginBottom: 20,
          }}
        >
          {scene.icon}
        </div>
      )}

      {/* Point Pill */}
      <div
        style={{
          display: "inline-block",
          padding: "10px 28px",
          borderRadius: 24,
          backgroundColor: "rgba(72, 191, 145, 0.2)",
          border: "1px solid rgba(72, 191, 145, 0.6)",
          color: "#48BF91",
          fontFamily: "system-ui, -apple-system, sans-serif",
          fontWeight: 800,
          fontSize: 22,
          letterSpacing: "0.08em",
          marginBottom: 16,
          textTransform: "uppercase",
        }}
      >
        {scene.title}
      </div>

      {/* Subtitle / Key Concept */}
      {scene.subtitle && (
        <div
          style={{
            fontFamily: "system-ui, -apple-system, sans-serif",
            fontWeight: 800,
            fontSize: 44,
            lineHeight: 1.25,
            color: "#FFFFFF",
            textShadow: "0 6px 24px rgba(0, 0, 0, 0.8)",
            padding: "0 24px",
          }}
        >
          {scene.subtitle}
        </div>
      )}
    </div>
  );
};
