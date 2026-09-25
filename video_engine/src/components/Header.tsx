import React from "react";
import { interpolate, useCurrentFrame, useVideoConfig } from "remotion";

export const Header: React.FC<{ kicker?: string }> = ({ kicker = "PSICOLOGÍA CLÍNICA" }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  // Progress line from 0% to 100%
  const progress = interpolate(frame, [0, durationInFrames], [0, 1080], {
    extrapolateRight: "clamp",
  });

  return (
    <div style={{ position: "absolute", top: 0, left: 0, width: 1080, zIndex: 50 }}>
      {/* Top Progress Bar */}
      <div style={{ width: 1080, height: 8, backgroundColor: "rgba(255, 255, 255, 0.1)" }}>
        <div
          style={{
            width: progress,
            height: "100%",
            background: "linear-gradient(90deg, #E9806E 0%, #48BF91 100%)",
            boxShadow: "0 0 16px rgba(233, 128, 110, 0.8)",
          }}
        />
      </div>

      {/* Glassmorphic Brand Tag */}
      <div
        style={{
          marginTop: 60,
          marginLeft: "auto",
          marginRight: "auto",
          width: "max-content",
          display: "flex",
          alignItems: "center",
          gap: 14,
          padding: "14px 28px",
          borderRadius: 40,
          backgroundColor: "rgba(18, 42, 34, 0.75)",
          border: "1px solid rgba(255, 255, 255, 0.15)",
          backdropFilter: "blur(20px)",
          boxShadow: "0 12px 32px rgba(0, 0, 0, 0.4)",
        }}
      >
        <span style={{ fontSize: 26 }}>🌿</span>
        <span
          style={{
            fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
            fontWeight: 800,
            fontSize: 22,
            letterSpacing: "0.08em",
            color: "#FFFFFF",
            textTransform: "uppercase",
          }}
        >
          CENTRO PAZ
        </span>
        <span style={{ color: "rgba(255, 255, 255, 0.3)", fontSize: 18 }}>•</span>
        <span
          style={{
            fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
            fontWeight: 700,
            fontSize: 19,
            letterSpacing: "0.06em",
            color: "#E9806E",
            textTransform: "uppercase",
          }}
        >
          {kicker}
        </span>
      </div>
    </div>
  );
};
