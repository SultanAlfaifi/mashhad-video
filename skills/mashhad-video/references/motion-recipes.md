# Motion recipes

Read only the recipe relevant to the shot. These are original staging patterns, not bundled implementations. Engine or community-skill capabilities must be checked in the actual environment. Mixing all techniques into one film is rarely useful.

Time movement to meaning, legibility, and physical cause. Accent selected actions with an original or appropriately licensed effect; a cut or entrance can remain silent. These recipes do not imply a music track, beat grid, tonal pad, or rhythmic sound loop.

## Kinetic typography

Stage a phrase around its meaningful word. Establish the phrase, shift emphasis at the spoken stress, then let the emphasized word motivate the next composition. Use scale, weight, position, masking, or negative space selectively. **Invariant:** the viewer can read the complete intended message. **Pitfalls:** every word receives equal spectacle; words leave before comprehension; scaling changes the anchor; Arabic letters become disconnected. Animate Arabic words or shaped text masks by default.

## Data morph

Transform one representation into another to reveal the same underlying relationship: dots gather into grouped bars; a highlighted bar becomes a detail panel. Keep entity identifiers, values, color meaning, and a persistent label through the handoff. **Invariant:** data remains truthful and its mapping understandable. **Pitfalls:** arbitrary intermediate geometry implies false quantities; labels detach; changing axes suggests growth. Crossfade or stage the change when a morph would falsely imply equivalence. Verify SVG path correspondence and winding; MorphSVG offers controls for problematic correspondence [1].

## Continuous UI B-roll

Choose a carrier object: selected row, task card, capsule, or cursor-led panel. Retain its anchor and identity while the surrounding interface changes. Settle, perform an intentional interaction, show the consequence, then travel. Hide a component swap during an occlusion or shape match when needed. **Invariant:** state changes follow an understandable cause. **Pitfalls:** implausible fake UI, racing cursors, decorative clicking, simultaneous competing panels. Product claims need support from the actual product.

## Documentary collage

Establish a visual hierarchy between evidence, annotation, and atmosphere. Reveal a document detail, connect it to the narration, then widen to context. Depth can separate layers, while restrained shadows make them belong together. **Invariant:** source material keeps its meaning and attribution. **Pitfalls:** unreadable screenshots, fabricated archival material presented as fact, constant camera drift, ornamental paper noise overwhelming evidence.

## Text behind a subject

Use a clean foreground matte over the text layer and background plate. Establish readable text before or after intentional occlusion; use the camera to create depth without repeatedly hiding the key word. **Invariant:** the sentence remains recoverable and the subject edge stable. **Pitfalls:** flickering hair masks, transparency halos, wrong parallax, perspective-distorted captions. Test the matte over high-contrast text; simplify occlusion when the source cannot support clean separation.

## Painterly p5 reveal

Use a stable stroke field derived from image structure and seeded variation. Reveal ordered stroke groups with a clear sweep, letting the subject emerge before decorative texture. **Invariant:** seeking to the same timestamp reproduces the same image. **Pitfalls:** per-frame random flicker, accumulated state depending on playback history, unreadable painted lettering. Seed randomness [2]; derive stroke visibility from time or deterministic replay. Do not assume an alphabet-specific handwriting routine supports Arabic.

## Procedural 3D

Begin with silhouette, light, and camera blocking. Use instancing, curves, or generated geometry where repetition or transformation serves the idea. Reserve detail for the hero view. **Invariant:** spatial relations remain intelligible across the cut. **Pitfalls:** excessive depth-of-field hides the product; reflective materials lack readable light shapes; simulations change across renders. Bake relevant simulations, verify transparency/color handoff, and render a difficult short segment before committing the full sequence.

Primary references checked 2026-10-09: [1] [GSAP MorphSVG](https://gsap.com/docs/v3/Plugins/MorphSVGPlugin/); [2] [p5 randomSeed](https://p5js.org/reference/p5/randomSeed/). These sources support mechanics, not an aesthetic quality guarantee.
