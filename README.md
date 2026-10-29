# Bengaluru — ಬೆಂಗಳೂರು

A real-time 3D model of central Bengaluru built with [Three.js](https://threejs.org),
playable in a desktop browser and in VR on a Meta Quest headset.

**Everything is in one file: `index.html`.** No build step, no dependencies to
install, no server-side code. Three.js is loaded from a CDN at runtime.

## What's in it

**Landmarks** — Vidhana Soudha, Attara Kacheri (the High Court), Bangalore Palace,
UB City, the Lalbagh Glass House with Kempegowda's watchtower, the Bull Temple at
Basavanagudi, Brigade Road, Ulsoor Lake and the Namma Metro Purple Line viaduct.

**Traffic** — a left-hand-drive simulation with 38 signalled junctions and 124 zebra
crossings. Vehicles follow an IDM car-following model, hold lane discipline, turn
through junctions, stop at red lights, and yield to pedestrians on a crossing.
Pedestrians walk a sidewalk graph, wait for the walk phase, and cross together.

**Life** — tennis rallies on six courts in Cubbon Park, joggers, yoga groups, street
vendors, cows, boats on Ulsoor Lake and birds overhead.

**Atmosphere** — a full day/night cycle, a monsoon toggle with rain and thunder, and
positional audio (traffic, horns, birds, a temple bell, tennis).

## Running it

Open `index.html` in any modern browser. It needs an internet connection the first
time so it can fetch Three.js from the CDN.

To serve it locally:

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Publishing it on GitHub Pages

1. Push this folder to a repository.
2. In the repository, go to **Settings → Pages**.
3. Under **Source**, choose **Deploy from a branch**, pick your default branch
   (usually `main`) and the `/ (root)` folder, then **Save**.
4. After a minute the site is live at `https://<username>.github.io/<repo>/`.

If you put these files in a subfolder rather than the repository root, the URL
gains that folder on the end: `https://<username>.github.io/<repo>/<folder>/`.

## VR on a Meta Quest

Open the published `https://` URL in the **Meta Quest Browser** and press
**Enter VR**. WebXR requires a secure context, so it has to be `https://` or
`localhost` — opening the file directly from disk will not offer VR.

In the headset: the trigger teleports, the left stick walks, the right stick snap-turns,
**X** opens a wrist menu (landmarks, time of day, rain, flying, the metro ride) and
**A** toggles flying. There are Performance / Balanced / Ultra presets on the desktop
page before you enter.

## Desktop controls

| Control | Action |
|---|---|
| Drag | Look around |
| Scroll | Zoom |
| `W` `A` `S` `D` | Walk (in Walk mode) |
| `Shift` | Run |
| `F` | Toggle Walk mode |
| `H` | Hide the interface |

The dock along the bottom switches between Orbit, Walk, Metro ride and Courts views,
sets the time of day, toggles the monsoon and turns sound on.

## URL parameters

Handy for linking to a particular view:

`?t=20.5` time of day in hours · `?rain=1` monsoon on · `?mode=walk&at=tennis` start
walking at a landmark · `?cam=x,y,z,tx,ty,tz` explicit camera and target.

## Credits

Built with [Three.js](https://threejs.org) (MIT). All geometry is generated
procedurally in code — there are no external models or textures.
