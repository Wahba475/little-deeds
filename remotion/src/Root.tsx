import {Composition} from 'remotion';
import {Short, ShortProps} from './Short';

// Props come from a JSON file: npx remotion render ... --props=public/<id>.json
const defaults: ShortProps = {video: 'scene.mp4', duration: 5, words: [], pill: '', refs: [], rtl: false};

export const Root = () => (
  <Composition
    id="Short"
    component={Short}
    width={1080}
    height={1920}
    fps={30}
    durationInFrames={150}
    defaultProps={defaults}
    calculateMetadata={({props}) => ({durationInFrames: Math.ceil(props.duration * 30)})}
  />
);
