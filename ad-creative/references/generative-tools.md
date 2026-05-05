# Generative Tools for Ad Visuals

Reference for image, video, voice, and code-based tools used in ad creative production.

---

## Image Generation

| Tool              | Best For                                  | Notes                                      |
|-------------------|-------------------------------------------|--------------------------------------------|
| Flux (Black Forest Labs) | High-quality static ad images      | Strong photorealism, good prompt adherence |
| Ideogram          | Text-on-image ads                         | Best-in-class legible text in images       |
| Gemini (Imagen)   | Versatile, Google ecosystem               | Good for iterating quickly                 |
| DALL·E 3          | Concept exploration                       | Via ChatGPT or API                         |

**Recommended for ads:** Flux for product/lifestyle images; Ideogram when your creative needs readable text embedded in the image.

**Platform image dimensions (required):**

| Platform         | Placement              | Dimensions         | Aspect Ratio |
|------------------|------------------------|--------------------|--------------|
| Meta             | Feed (square)          | 1080 × 1080 px     | 1:1          |
| Meta             | Feed (landscape)       | 1200 × 628 px      | 1.91:1       |
| Meta             | Stories / Reels        | 1080 × 1920 px     | 9:16         |
| Google Display   | Leaderboard            | 728 × 90 px        | 8:1          |
| Google Display   | Medium rectangle       | 300 × 250 px       | 6:5          |
| LinkedIn         | Single image ad        | 1200 × 627 px      | 1.91:1       |
| TikTok           | In-feed video          | 1080 × 1920 px     | 9:16         |
| Twitter/X        | Card image             | 1200 × 675 px      | 16:9         |

---

## Video Generation

| Tool      | Best For                               | Notes                             |
|-----------|----------------------------------------|-----------------------------------|
| Veo 2 (Google) | High-quality, longer clips        | Best quality at time of writing   |
| Kling     | Fast iteration, good motion           | Strong for product demos          |
| Runway    | Creative / stylized video             | Good for brand storytelling       |
| Sora      | Cinematic quality                     | OpenAI, best for hero creative    |
| Higgsfield| Human motion, realistic scenes        | Good for lifestyle / UGC-style    |

**Recommended workflow:**
1. Use Veo or Sora for hero/launch creative (quality matters most)
2. Use Kling for rapid iteration and A/B testing variants
3. Use Remotion (below) for templated, data-driven production at scale

---

## Voice & Audio

| Tool            | Best For                           |
|-----------------|------------------------------------|
| ElevenLabs      | Voiceovers, voice cloning, multilingual |
| OpenAI TTS      | Fast, clean narration              |
| Cartesia        | Low-latency, real-time voice       |

**Workflow:** Generate script → run through ElevenLabs → sync to video in editing tool or Remotion.

---

## Code-Based Video at Scale — Remotion

Remotion lets you build video templates in React and render them programmatically. This is the right tool when you need:
- 50+ ad variations with the same template but different headlines/images
- Data-driven video (e.g., personalized ads, dynamic pricing)
- Consistent branding across a large creative batch

**Basic workflow:**
1. Design and validate one video template in Remotion
2. Build a data feed (CSV or JSON) with variation-specific content
3. Batch render with `@remotion/renderer` — outputs one video per row
4. Upload rendered videos to your ad platform

**When to use Remotion vs. generative video:**
- Use **generative tools** (Veo, Kling) for new angles, new concepts, hero creative
- Use **Remotion** once a winning template is identified and you need scale

---

## Recommended Production Workflow

For a full-scale creative sprint:

```
1. Ideation & copy → ad-creative skill (this skill)
2. Hero image/video → Flux / Veo / Sora (quality, exploratory)
3. Review & identify winners → human review + early performance data
4. Build Remotion template → based on winning creative format
5. Batch produce at scale → Remotion + data feed
6. Iterate → new angles via AI tools, proven templates via Remotion
```

This approach balances quality (AI generation for new concepts) with cost-efficiency (Remotion for proven formats at scale).
