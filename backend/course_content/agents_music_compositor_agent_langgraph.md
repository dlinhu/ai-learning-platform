# 音乐作曲Agent / Music Compositor Agent

## Overview / 概述

Build an agent that assists in music composition. / 构建协助音乐创作的Agent。

## Key Knowledge Points / 核心知识点

### 1. 音乐创作辅助 / Music Composition Assistance

**English:** Agent generates music composition suggestions and structures based on style and parameters.

**中文:** Agent根据风格和参数生成音乐创作建议和结构。

**Key Concepts / 核心概念:**
- Style analysis / 风格分析
- Composition structure / 作曲结构
- Creative suggestions / 创意建议

**Example / 示例:**
```python
style_params = analyze_style(genre, mood)
composition = generate_composition(style_params, duration)
# → Generate music composition suggestions

```

---

### 2. 音乐理论应用 / Music Theory Application

**English:** Apply music theory knowledge including chord progressions, tonality, and rhythm patterns.

**中文:** 应用音乐理论知识，包括和弦进程、调性和节奏模式。

**Key Concepts / 核心概念:**
- Chord progressions / 和弦进程
- Key signatures / 调号
- Rhythm patterns / 节奏模式

**Example / 示例:**
```python
def generate_chord_progression(key, style, num_bars):
    theory_rules = load_music_theory(style)
    chords = []
    current_chord = theory_rules['tonic'][key]
    for i in range(num_bars):
        next_chord = select_next_chord(current_chord, theory_rules['progressions'])
        chords.append(next_chord)
        current_chord = next_chord
    return chords
# → Generate chord progression based on music theory

```

---

### 3. MIDI生成与输出 / MIDI Generation & Output

**English:** Convert composed music to MIDI format, supporting export and playback.

**中文:** 将创作的音乐转换为MIDI格式，支持导出和播放。

**Key Concepts / 核心概念:**
- MIDI format / MIDI格式
- Note representation / 音符表示
- Export options / 导出选项

**Example / 示例:**
```python
from midiutil import MIDIFile

def create_midi(composition, output_path):
    midi = MIDIFile(1)
    track = 0
    time = 0
    midi.addTrackName(track, time, composition.title)
    midi.addTempo(track, time, composition.tempo)
    
    for note in composition.notes:
        midi.addNote(track, 0, note.pitch, note.start, note.duration, note.velocity)
    
    with open(output_path, 'wb') as f:
        midi.writeFile(f)
# → Create MIDI file from composition

```

---

## Summary / 总结

This lesson covered key AI Agent concepts. Practice these techniques to build better intelligent systems.

本课程涵盖了关键AI Agent技术。练习这些技术以构建更好的智能系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own agents / 构建自己的Agent
3. Explore advanced patterns / 探索高级模式
