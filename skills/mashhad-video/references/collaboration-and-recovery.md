# Collaboration and recovery

Use parallel production for independent shots, source research, or an independent review; avoid splitting a tiny composition into a team.

## Handoff

Give a contributor the selected brief/styleframe, exact shot interval, geometry, allowed engine/version, supplied assets and exact text, its owned files, integration format, and expected outputs. Ask for source paths, rendered output if feasible, checks performed, and unresolved limitations. Do not make multiple contributors edit the master timeline, shared styles, or final soundtrack concurrently.

An independent critic receives the brief, actual rendered media/frames, and review criteria. Do not feed it the intended verdict or ask it to confirm the creator's enthusiasm. A visual critic that only sees stills can assess composition and text but must not claim to assess pacing or sound. Resolve conflicting feedback against the user's intended effect and concrete evidence.

## Checkpoint and resume

Record the last finished shot, current render command/version, reviewed ranges, asset paths, and outstanding issue. Resume from verified artifacts when the user says to continue. A pause stops new work and saves the checkpoint; elapsed time is not permission to resume.

For a failed command, inspect the error and any partial output before retrying. Give outputs versioned filenames until validated, and preserve the previous good render. For an editor/MCP timeout, inspect actual application state first because the mutation may have succeeded. Never replay an entire edit sequence blindly.

For a repeated failed approach, change the failing mechanism or choose a compatible simpler route. A missing proprietary editor cannot be solved by inventing its tools. Propose a substitute only with its effect on editability/appearance made clear. Do not claim a fallback is equivalent when it changes the requested deliverable.

## Dependency drift

Use the project's lockfile and known working versions. Refresh the selected adapter's primary documentation when a command fails due to version drift, when installing/upgrading, or when the user requests the latest workflow. A successful smoke render is required before adopting an upgrade for a long job. Preserve rollback paths and do not update every engine during an unrelated edit.
