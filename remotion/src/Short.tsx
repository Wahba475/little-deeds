import {AbsoluteFill, OffthreadVideo, Audio, staticFile, useCurrentFrame, useVideoConfig, interpolate, Easing} from 'remotion';
import {loadFont} from '@remotion/fonts';
import {Captions} from './Captions';

loadFont({family: 'ArCap', url: staticFile('fonts/ar.ttf'), weight: '100 900'});

// words: [text, startSec, endSec, flag?]  flag "q" = hadith quote styling
export type Word = [string, number, number, string?];
export type Ref = {text: string; from: number; to: number};
export type ShortProps = {video: string; voice?: string; duration: number; words: Word[]; pill: string; refs: Ref[]; rtl: boolean};

const Pill: React.FC<{text: string}> = ({text}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  if (!text) return null;
  return (
    <div style={{position: 'absolute', top: 215, width: '100%', display: 'flex', justifyContent: 'center'}}>
      <div style={{padding: '16px 34px', borderRadius: 22, background: 'rgba(120,30,20,.85)', border: '2px solid rgba(255,255,255,.18)', color: '#fff', font: '900 46px Inter, sans-serif',
        scale: interpolate(f, [0, 0.12 * fps, 0.25 * fps], [0.6, 1.15, 1], {extrapolateRight: 'clamp', easing: Easing.bezier(0.16, 1, 0.3, 1)})}}>{text}</div>
    </div>
  );
};

const Chip: React.FC<{refs: Ref[]; rtl: boolean}> = ({refs, rtl}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const t = f / fps;
  const r = refs.find((x) => t >= x.from - 0.25 && t < x.to + 0.2);
  if (!r) return null;
  const o = Math.min(interpolate(t, [r.from, r.from + 0.3], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}), interpolate(t, [r.to - 0.2, r.to], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}));
  return (
    <div style={{position: 'absolute', top: 318, width: '100%', display: 'flex', justifyContent: 'center', opacity: o}}>
      <div dir={rtl ? 'rtl' : 'ltr'} style={{padding: '12px 28px', borderRadius: 18, background: 'rgba(40,24,18,.78)', border: '2px solid rgba(255,214,140,.7)', color: '#ffe2a8', font: `800 36px ${rtl ? 'ArCap' : 'Inter'}, sans-serif`}}>{r.text}</div>
    </div>
  );
};

export const Short: React.FC<ShortProps> = ({video, voice, words, pill, refs, rtl}) => (
  <AbsoluteFill style={{background: '#000'}}>
    <OffthreadVideo src={staticFile(video)} muted />
    <Pill text={pill} />
    <Chip refs={refs} rtl={rtl} />
    <Captions words={words} rtl={rtl} />
    {voice ? <Audio src={staticFile(voice)} /> : null}
  </AbsoluteFill>
);
