import React from "react";
import { Composition } from "remotion";
import { PsychologyShort } from "./PsychologyShort";
import { PsychologyShortProps } from "./types";

const defaultProps: PsychologyShortProps = {
  title: "3 Señales de TDAH en Adultos",
  kicker: "TDAH EN ADULTOS",
  hookText: "3 cosas que parecían flojera pero eran TDAH 🧠",
  audioUrl: "",
  durationSec: 35,
  therapistName: "Valentina Castro Núñez",
  phoneDisplay: "+56 9 6516 3893",
  scenes: [
    {
      id: "s1",
      title: "Punto 1: Parálisis Ejecutiva",
      subtitle: "Tu cerebro necesita un nivel mínimo de dopamina para 'arrancar'.",
      icon: "⚡",
      startSec: 4.0,
      endSec: 13.0,
    },
    {
      id: "s2",
      title: "Punto 2: Masking & Cansancio",
      subtitle: "El esfuerzo inconsciente de sobre-adaptarte para encajar.",
      icon: "🎭",
      startSec: 13.0,
      endSec: 22.0,
    },
    {
      id: "s3",
      title: "Punto 3: Sensibilidad al Rechazo",
      subtitle: "Miedo intenso a equivocarte o recibir una crítica.",
      icon: "❤️‍🩹",
      startSec: 22.0,
      endSec: 30.5,
    },
  ],
  words: [],
};

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="PsychologyShort"
        component={PsychologyShort}
        durationInFrames={30 * 35}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultProps}
        calculateMetadata={({ props }) => {
          const durSec = props.durationSec || 35;
          return {
            durationInFrames: Math.ceil(durSec * 30),
            props,
          };
        }}
      />
    </>
  );
};
