export interface WordTimestamp {
  word: string;
  start: number; // in seconds
  end: number;   // in seconds
}

export interface ShortScene {
  id: string;
  title: string;
  subtitle?: string;
  icon?: string;
  startSec: number;
  endSec: number;
}

export interface PsychologyShortProps {
  title: string;
  kicker: string;
  audioUrl: string;
  durationSec: number;
  hookText: string;
  scenes: ShortScene[];
  words: WordTimestamp[];
  therapistName?: string;
  phoneDisplay?: string;
}
