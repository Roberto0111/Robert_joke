#!/bin/zsh
set -euo pipefail

ROOT="${0:A:h}"
FFMPEG="${FFMPEG_BIN:-/opt/homebrew/bin/ffmpeg}"
FFPROBE="${FFPROBE_BIN:-/opt/homebrew/bin/ffprobe}"
VOICE_DIR="$ROOT/audio"
CLIP_DIR="$ROOT/output/clips"
OUT="$ROOT/output/roberto_joke_pilot_001.mp4"

mkdir -p "$VOICE_DIR" "$CLIP_DIR"

say -v 'Eddy (中文（台灣）)' -r 168 -o "$VOICE_DIR/01_cat_late.aiff" '起床，你要遲到了。'
say -v 'Reed (中文（台灣）)' -r 178 -o "$VOICE_DIR/02_roberto_who.aiff" '你誰啊？怎麼又進我家？'
say -v 'Eddy (中文（台灣）)' -r 164 -o "$VOICE_DIR/03_cat_work.aiff" '快去上班。'
say -v 'Reed (中文（台灣）)' -r 172 -o "$VOICE_DIR/04_roberto_jobless.aiff" '我失業三個月了，上什麼班？'
say -v 'Reed (中文（台灣）)' -r 168 -o "$VOICE_DIR/05_roberto_owner.aiff" '你到底是誰養的？'
say -v 'Eddy (中文（台灣）)' -r 145 -o "$VOICE_DIR/06_cat_landlord.aiff" '房東。'
say -v 'Grandpa (中文（台灣）)' -r 154 -o "$VOICE_DIR/07_landlord_care.aiff" '我只是請牠每天看看，你還活著沒有。'
say -v 'Reed (中文（台灣）)' -r 146 -o "$VOICE_DIR/08_roberto_touched.aiff" '原來，還是有人關心我。'
say -v 'Eddy (中文（台灣）)' -r 146 -o "$VOICE_DIR/09_cat_rent.aiff" '順便提醒你，房租也還活著。'

make_clip() {
  local image="$1"
  local seconds="$2"
  local output="$3"
  local frames=$(( seconds * 30 ))
  "$FFMPEG" -hide_banner -loglevel error -y -loop 1 -i "$image" -t "$seconds" \
    -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,zoompan=z='min(zoom+0.00045,1.055)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=${frames}:s=1080x1920:fps=30,format=yuv420p" \
    -an -c:v libx264 -preset medium -crf 18 "$output"
}

make_clip "$ROOT/frames/01_cat_on_chest.png" 7 "$CLIP_DIR/01.mp4"
make_clip "$ROOT/frames/02_doorway.png" 3 "$CLIP_DIR/02.mp4"
make_clip "$ROOT/frames/01_cat_on_chest.png" 3 "$CLIP_DIR/03.mp4"
make_clip "$ROOT/frames/03_phone_argument.png" 9 "$CLIP_DIR/04.mp4"
make_clip "$ROOT/frames/04_landlord_tag.png" 7 "$CLIP_DIR/05.mp4"
make_clip "$ROOT/frames/05_landlord_call.png" 10 "$CLIP_DIR/06.mp4"
make_clip "$ROOT/frames/06_rent_punchline.png" 11 "$CLIP_DIR/07.mp4"

cat > "$CLIP_DIR/concat.txt" <<EOF
file '$CLIP_DIR/01.mp4'
file '$CLIP_DIR/02.mp4'
file '$CLIP_DIR/03.mp4'
file '$CLIP_DIR/04.mp4'
file '$CLIP_DIR/05.mp4'
file '$CLIP_DIR/06.mp4'
file '$CLIP_DIR/07.mp4'
EOF

"$FFMPEG" -hide_banner -loglevel error -y -f concat -safe 0 -i "$CLIP_DIR/concat.txt" -c copy "$CLIP_DIR/silent.mp4"

MUSIC="$ROOT/../../posts/2026-07-31_2030/playful_soundtrack.wav"
"$FFMPEG" -hide_banner -loglevel error -y \
  -i "$CLIP_DIR/silent.mp4" \
  -stream_loop -1 -i "$MUSIC" \
  -i "$VOICE_DIR/01_cat_late.aiff" \
  -i "$VOICE_DIR/02_roberto_who.aiff" \
  -i "$VOICE_DIR/03_cat_work.aiff" \
  -i "$VOICE_DIR/04_roberto_jobless.aiff" \
  -i "$VOICE_DIR/05_roberto_owner.aiff" \
  -i "$VOICE_DIR/06_cat_landlord.aiff" \
  -i "$VOICE_DIR/07_landlord_care.aiff" \
  -i "$VOICE_DIR/08_roberto_touched.aiff" \
  -i "$VOICE_DIR/09_cat_rent.aiff" \
  -filter_complex "
    [0:v]ass='$ROOT/subtitles.ass'[v];
    [1:a]atrim=0:50,volume=0.07,afade=t=in:st=0:d=0.5,afade=t=out:st=48:d=2[bg];
    [2:a]adelay=550:all=1,volume=1.22[a2];
    [3:a]adelay=3350:all=1,volume=1.15[a3];
    [4:a]adelay=10550:all=1,volume=1.22[a4];
    [5:a]adelay=13550:all=1,volume=1.15[a5];
    [6:a]adelay=22100:all=1,volume=1.15[a6];
    [7:a]adelay=26200:all=1,volume=1.28[a7];
    [8:a]adelay=29200:all=1,volume=1.18[a8];
    [9:a]adelay=35100:all=1,volume=1.15[a9];
    [10:a]adelay=39400:all=1,volume=1.28[a10];
    [bg][a2][a3][a4][a5][a6][a7][a8][a9][a10]amix=inputs=10:duration=longest:normalize=0,alimiter=limit=0.95,atrim=0:50[a]
  " \
  -map '[v]' -map '[a]' -t 50 -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 192k \
  -movflags +faststart -pix_fmt yuv420p -r 30 "$OUT"

"$FFPROBE" -v error -show_entries format=duration,size -show_entries stream=width,height,r_frame_rate,codec_name -of json "$OUT"
