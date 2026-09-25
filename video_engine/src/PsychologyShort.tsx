import React from "react";
import { Audio, useCurrentFrame, useVideoConfig } from "remotion";
import { PsychologyShortProps } from "./types";
import { Background } from "./components/Background";
import { Header } from "./components/Header";
import { HookCard } from "./components/HookCard";
import { PointCard } from "./components/PointCard";
import { SubtitlesKaraoke } from "./components/SubtitlesKaraoke";
import { OutroCard } from "./components/OutroCard";

export const PsychologyShort: React.FC<PsychologyShortProps> = ({
  kicker,
  hookText,
  audioUrl,
  scenes,
  words,
  therapistName,
  phoneDisplay,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const currentSec = frame / fps;
  const durationSec = durationInFrames / fps;

  // Identify active scene
  const activeScene = scenes.find(
    (s) => currentSec >= s.startSec && currentSec < s.endSec
  );

  const isOutro = currentSec >= durationSec - 4.5;
  const isHook = currentSec < (scenes[0]?.startSec || 4.0);

  const sceneRelativeFrame = activeScene
    ? Math.max(0, frame - Math.floor(activeScene.startSec * fps))
    : 0;
  const outroRelativeFrame = Math.max(0, frame - Math.floor((durationSec - 4.5) * fps));

  return (
    <div
      style={{
        width: 1080,
        height: 1920,
        position: "relative",
        overflow: "hidden",
      }}
    >
      {/* 1. Cinematic Animated Background */}
      <Background />

      {/* 2. Top Header & Progress Bar */}
      <Header kicker={kicker} />

      {/* 3. Visual Cards Layer */}
      {isOutro ? (
        <OutroCard
          therapistName={therapistName}
          phoneDisplay={phoneDisplay}
          relativeFrame={outroRelativeFrame}
        />
      ) : isHook ? (
        <HookCard hookText={hookText} category={kicker} />
      ) : activeScene ? (
        <PointCard scene={activeScene} relativeFrame={sceneRelativeFrame} />
      ) : null}

      {/* 4. Real-time Karaoke Subtitles (Hide during Outro) */}
      {!isOutro && <SubtitlesKaraoke words={words} />}

      {/* 5. Voice Audio Track */}
      {audioUrl && <Audio src={audioUrl} />}
    </div>
  );
};
