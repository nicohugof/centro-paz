import React from "react";
import { useCurrentFrame, useVideoConfig } from "remotion";
import { WordTimestamp } from "../types";

export const SubtitlesKaraoke: React.FC<{ words: WordTimestamp[] }> = ({ words }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const currentTime = frame / fps;

  if (!words || words.length === 0) return null;

  // Find the index of the currently active word
  const activeWordIndex = words.findIndex(
    (w) => currentTime >= w.start && currentTime <= w.end
  );

  // If no word is currently active, find the closest preceding or upcoming word within 1.0s
  let targetIndex = activeWordIndex;
  if (targetIndex === -1) {
    targetIndex = words.findIndex((w) => w.start > currentTime);
    if (targetIndex > 0 && currentTime - words[targetIndex - 1].end < 0.8) {
      targetIndex = targetIndex - 1;
    }
  }

  if (targetIndex === -1 && words.length > 0 && currentTime < words[0].start) {
    targetIndex = 0;
  }
  if (targetIndex === -1 && words.length > 0) {
    targetIndex = words.length - 1;
  }

  // Create a visible window of ~4-5 words around the active word
  const windowSize = 4;
  const chunkStart = Math.max(0, Math.floor(targetIndex / windowSize) * windowSize);
  const chunkWords = words.slice(chunkStart, chunkStart + windowSize);

  return (
    <div
      style={{
        position: "absolute",
        top: 1040,
        left: 60,
        width: 960,
        display: "flex",
        flexWrap: "wrap",
        justifyContent: "center",
        alignItems: "center",
        gap: "12px 18px",
        padding: "24px 32px",
        borderRadius: 32,
        backgroundColor: "rgba(10, 24, 19, 0.82)",
        border: "1px solid rgba(255, 255, 255, 0.12)",
        backdropFilter: "blur(24px)",
        boxShadow: "0 16px 48px rgba(0, 0, 0, 0.6)",
        zIndex: 60,
      }}
    >
      {chunkWords.map((item, idx) => {
        const isCurrent = currentTime >= item.start && currentTime <= item.end;
        const isPast = currentTime > item.end;

        return (
          <span
            key={`${item.word}-${item.start}-${idx}`}
            style={{
              fontFamily:
                "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
              fontWeight: isCurrent ? 900 : 700,
              fontSize: isCurrent ? 44 : 38,
              color: isCurrent ? "#FFD166" : isPast ? "#FFFFFF" : "rgba(255, 255, 255, 0.55)",
              padding: isCurrent ? "4px 14px" : "2px 6px",
              borderRadius: 14,
              backgroundColor: isCurrent ? "rgba(233, 128, 110, 0.35)" : "transparent",
              border: isCurrent ? "1px solid rgba(233, 128, 110, 0.7)" : "1px solid transparent",
              transform: isCurrent ? "scale(1.08)" : "scale(1.0)",
              transition: "all 0.1s ease-out",
              textShadow: "0 4px 16px rgba(0, 0, 0, 0.9)",
              display: "inline-block",
            }}
          >
            {item.word}
          </span>
        );
      })}
    </div>
  );
};
