import {useMemo} from 'react';
import {useCurrentFrame, useVideoConfig, interpolate, Easing} from 'remotion';
import {createTikTokStyleCaptions, Caption} from '@remotion/captions';
import type {Word} from './Short';

// TikTok-style pages: 1-3 words, active word yellow, hadith words cream/gold.
// Arabic: dir="rtl" on the line and animate whole words only (never split letters).
export const Captions: React.FC<{words: Word[]; rtl: boolean}> = ({words, rtl}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const ms = (f / fps) * 1000;
  const quote = useMemo(() => new Set(words.filter((w) => w[3] === 'q').map((w) => Math.round(w[1] * 1000))), [words]);
  const {pages} = useMemo(() => {
    const caps: Caption[] = words.map((w, i) => ({text: (i ? ' ' : '') + w[0], startMs: w[1] * 1000, endMs: w[2] * 1000, timestampMs: ((w[1] + w[2]) / 2) * 1000, confidence: null}));
    return createTikTokStyleCaptions({captions: caps, combineTokensWithinMilliseconds: rtl ? 900 : 700});
  }, [words, rtl]);
  const page = pages.find((p, i) => ms >= p.startMs - 40 && ms < (pages[i + 1] ? Math.min(pages[i + 1].startMs - 40, p.startMs + p.durationMs + 900) : p.startMs + p.durationMs + 500));
  if (!page) return null;
  const pop = interpolate(ms, [page.startMs - 40, page.startMs + 120], [0.82, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.bezier(0.16, 1, 0.3, 1)});
  return (
    <div dir={rtl ? 'rtl' : 'ltr'} style={{position: 'absolute', left: 70, right: 70, top: rtl ? 1150 : 1190, textAlign: 'center', scale: pop,
      font: rtl ? '900 88px ArCap, sans-serif' : '900 96px Inter, sans-serif', lineHeight: rtl ? 1.45 : 1.08, color: '#fff', WebkitTextStroke: rtl ? '12px #05060c' : '14px #05060c', paintOrder: 'stroke', textShadow: '0 10px 26px rgba(0,0,0,.75)'}}>
      {page.tokens.map((tk, i) => {
        const on = ms >= tk.fromMs - 40 && ms < tk.toMs + 200;
        const isQ = quote.has(Math.round(tk.fromMs));
        const shown = ms >= tk.fromMs - 40;
        return (
          <span key={i} style={{display: 'inline-block', margin: '0 .1em', opacity: shown ? 1 : 0, color: on ? (isQ ? '#ffc24a' : '#ffd83d') : isQ ? '#fff3d6' : '#fff', scale: on ? 1.08 : 1}}>{tk.text.trim()}</span>
        );
      })}
    </div>
  );
};
