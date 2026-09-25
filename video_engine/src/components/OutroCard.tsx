import React from "react";
import { spring, useCurrentFrame, useVideoConfig } from "remotion";

export const OutroCard: React.FC<{
  therapistName?: string;
  phoneDisplay?: string;
  relativeFrame: number;
}> = ({
  therapistName = "Valentina Castro Núñez",
  phoneDisplay = "+56 9 6516 3893",
  relativeFrame,
}) => {
  const { fps } = useVideoConfig();

  const entrance = spring({
    frame: relativeFrame,
    fps,
    config: {
      damping: 14,
      stiffness: 120,
      mass: 0.8,
    },
  });

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
        transform: `scale(${entrance})`,
        opacity: Math.min(1, entrance * 1.3),
        zIndex: 50,
      }}
    >
      {/* Brand Badge */}
      <div
        style={{
          width: 110,
          height: 110,
          borderRadius: "50%",
          backgroundColor: "#16382D",
          border: "2px solid #E9806E",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          fontSize: 54,
          color: "#E9806E",
          boxShadow: "0 12px 36px rgba(0, 0, 0, 0.5)",
          marginBottom: 24,
        }}
      >
        Ψ
      </div>

      <div
        style={{
          fontFamily: "system-ui, -apple-system, sans-serif",
          fontWeight: 900,
          fontSize: 46,
          color: "#FFFFFF",
          lineHeight: 1.2,
          marginBottom: 12,
        }}
      >
        {therapistName}
      </div>

      <div
        style={{
          fontFamily: "system-ui, -apple-system, sans-serif",
          fontWeight: 700,
          fontSize: 26,
          color: "#48BF91",
          marginBottom: 32,
          letterSpacing: "0.04em",
        }}
      >
        Psicóloga Clínica · Enfoque Neuroafirmativo
      </div>

      {/* Badges Box */}
      <div
        style={{
          display: "flex",
          gap: 16,
          marginBottom: 40,
        }}
      >
        <div
          style={{
            padding: "12px 20px",
            borderRadius: 20,
            backgroundColor: "rgba(255, 255, 255, 0.08)",
            border: "1px solid rgba(255, 255, 255, 0.15)",
            color: "#FFFFFF",
            fontFamily: "system-ui, -apple-system, sans-serif",
            fontWeight: 700,
            fontSize: 20,
          }}
        >
          📍 Ñuñoa & Online
        </div>
        <div
          style={{
            padding: "12px 20px",
            borderRadius: 20,
            backgroundColor: "rgba(233, 128, 110, 0.2)",
            border: "1px solid rgba(233, 128, 110, 0.5)",
            color: "#E9806E",
            fontFamily: "system-ui, -apple-system, sans-serif",
            fontWeight: 700,
            fontSize: 20,
          }}
        >
          💳 Reembolso Isapre
        </div>
      </div>

      {/* WhatsApp Action Button */}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: 16,
          padding: "20px 40px",
          borderRadius: 40,
          background: "linear-gradient(135deg, #25D366 0%, #128C7E 100%)",
          color: "#FFFFFF",
          fontFamily: "system-ui, -apple-system, sans-serif",
          fontWeight: 900,
          fontSize: 28,
          boxShadow: "0 14px 40px rgba(37, 211, 102, 0.4)",
        }}
      >
        <span>💬</span>
        <span>WhatsApp: {phoneDisplay}</span>
      </div>

      <div
        style={{
          marginTop: 24,
          fontFamily: "system-ui, -apple-system, sans-serif",
          fontWeight: 600,
          fontSize: 20,
          color: "rgba(255, 255, 255, 0.6)",
        }}
      >
        Enlace directo en el perfil o en www.centropaz.cl
      </div>
    </div>
  );
};
