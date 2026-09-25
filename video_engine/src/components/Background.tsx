import React from "react";
import { interpolate, useCurrentFrame, useVideoConfig } from "remotion";

export const Background: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  // Floating ambient lighting oscillations
  const orb1X = interpolate(Math.sin(frame / 45), [-1, 1], [150, 450]);
  const orb1Y = interpolate(Math.cos(frame / 60), [-1, 1], [300, 700]);
  const orb1Scale = interpolate(Math.sin(frame / 30), [-1, 1], [0.9, 1.25]);

  const orb2X = interpolate(Math.cos(frame / 50), [-1, 1], [600, 950]);
  const orb2Y = interpolate(Math.sin(frame / 40), [-1, 1], [900, 1400]);
  const orb2Scale = interpolate(Math.cos(frame / 35), [-1, 1], [0.85, 1.3]);

  const orb3Y = interpolate(frame, [0, durationInFrames], [1600, 400]);

  return (
    <div
      style={{
        position: "absolute",
        width: 1080,
        height: 1920,
        backgroundColor: "#0A1713",
        overflow: "hidden",
      }}
    >
      {/* Deep gradient foundation */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          background:
            "radial-gradient(circle at 50% 20%, #153229 0%, #0D201A 45%, #07100D 100%)",
        }}
      />

      {/* Dynamic Aurora Orb 1 (Emerald / Forest Glow) */}
      <div
        style={{
          position: "absolute",
          left: orb1X,
          top: orb1Y,
          width: 650,
          height: 650,
          borderRadius: "50%",
          background: "radial-gradient(circle, rgba(46, 125, 96, 0.45) 0%, rgba(46, 125, 96, 0) 70%)",
          filter: "blur(90px)",
          transform: `scale(${orb1Scale})`,
          pointerEvents: "none",
        }}
      />

      {/* Dynamic Aurora Orb 2 (Warm Coral Accent) */}
      <div
        style={{
          position: "absolute",
          left: orb2X,
          top: orb2Y,
          width: 550,
          height: 550,
          borderRadius: "50%",
          background: "radial-gradient(circle, rgba(233, 128, 110, 0.35) 0%, rgba(233, 128, 110, 0) 70%)",
          filter: "blur(110px)",
          transform: `scale(${orb2Scale})`,
          pointerEvents: "none",
        }}
      />

      {/* Dynamic Ambient Orb 3 (Teal Light Lift) */}
      <div
        style={{
          position: "absolute",
          left: 300,
          top: orb3Y,
          width: 500,
          height: 500,
          borderRadius: "50%",
          background: "radial-gradient(circle, rgba(72, 191, 145, 0.2) 0%, rgba(72, 191, 145, 0) 70%)",
          filter: "blur(120px)",
          pointerEvents: "none",
        }}
      />

      {/* Subtle Cinematic Grid & Vignette */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          backgroundImage:
            "radial-gradient(rgba(255, 255, 255, 0.04) 1px, transparent 1px)",
          backgroundSize: "48px 48px",
          opacity: 0.7,
        }}
      />

      {/* Deep edge vignette */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          boxShadow: "inset 0 0 160px rgba(0, 0, 0, 0.85)",
          pointerEvents: "none",
        }}
      />
    </div>
  );
};
