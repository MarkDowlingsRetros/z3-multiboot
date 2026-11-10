# Z3 Multiboot

**Classic text adventures on six 1980s computers · Version 0.5 · November 2026**

Drop a story file on the page and a Commodore 64, Macintosh, Apple II, IBM PC, Amiga or NeXTSTEP boots it. Zork and the other classic Infocom adventures: any game made in the version 3 Z-machine format. Each machine comes with software of its own to play with, and the built-in Welcome Disk shows you around. It's one self-contained HTML file of about 132 KB (it still fits on a C64 floppy), with no install and no internet needed once it's loaded.

**▶ Play it here:** https://markdowlingsretros.github.io/z3-multiboot/

> An unofficial hobby project. Not affiliated with or endorsed by Microsoft, Activision, Infocom or the makers of any of the computers shown. Zork and other game names are trademarks of their owners.

![The Commodore 64 drawing the famous one-line maze](screenshots/c64.png)

## Six machines

Switch machines at any time from the bar at the top, or with **Option/Alt + 1–6**. Your game carries on exactly where it was.

| | | |
|---|---|---|
| ![Commodore 64](screenshots/c64.png) **Commodore 64** | ![Macintosh](screenshots/macintosh.png) **Macintosh** | ![Apple II](screenshots/apple-ii.png) **Apple II** |
| ![IBM PC](screenshots/ibm-pc.png) **IBM PC** | ![Amiga](screenshots/amiga.png) **Amiga** | ![NeXTSTEP](screenshots/nextstep.png) **NeXTSTEP** |

The machine looks are AI-made impressions built for fun. They are not the original systems or software, and the makers of those machines have nothing to do with this project.

## Every machine has something to play with

Each computer comes with its own software from the era, ready before you even load a game.

| Machine | What's on it |
|---|---|
| **Commodore 64** | A working BASIC prompt. `LOAD"$",8` then `LIST` shows the disk. `POKE 53280,0` and `POKE 53281,0` change the border and screen colours, `SYS 64738` resets the machine, and yes, `10 PRINT CHR$(205.5+RND(1)); : GOTO 10` then `RUN` draws the famous maze. |
| **Apple II** | Type `CATALOG` at the `]` prompt. `RUN ELIZA` for a chat with the 1966-style computer therapist, and `RUN LEDGER` for **LEDGER ][**, a working spreadsheet with formulas and `@SUM`. |
| **IBM PC** | **TSR King**, the resident utility: press Ctrl+Alt or F10 at any time for a calculator, notepad, calendar and ASCII table. |
| **Amiga** | A Workbench desktop with menus (Workbench, Disk, Special), SAY and the Boing! demo. Its hard drive, **DH0: Work**, keeps a copy of every game you load, so you can switch between them with a double-click. |
| **Macintosh** | The Calculator desk accessory under the ◆ menu, and resizable windows. |
| **NeXTSTEP** | The Dock, a File Viewer, and a working Terminal (type `help`). |

During a game these work on their own machine whenever the game doesn't use the same words. And there are easter eggs hidden throughout. We're not saying where.

## How to play

1. Open the link above, or download `index.html` and double-click it. It works in current versions of Safari, Chrome, Firefox and Edge.
2. The machine starts with no disk in the drive. First time? Click **Boot the Welcome Disk**. It's a ten-minute adventure set in a 1985 Melbourne house, and it shows you everything Z3 Multiboot can do.
3. To play a real game, get a version 3 story file (see Story files below) and drag it onto the page, or click **choose one**. The machine boots your game.

Type commands and press Return.

**Keys**

| Key | Does |
|---|---|
| Up / Down arrows | Previous commands |
| Page Up / Page Down | Scroll back through the story |
| Option/Alt + 1–6 | Switch machine |
| Option/Alt + Enter | Full screen |
| Any key | Skip a boot sequence |

## Story files

Z3 Multiboot is a player. No game is built in: you drop it in. The one exception is our own Welcome Disk, which you can boot from the empty-drive screen or **Options → Story file → Welcome Disk**.

- Works with **version 3** story files (`.z3`, sometimes `.dat`): the Zork trilogy and most Infocom games up to 1985, plus many modern games written for that format.
- **Zork I, II and III:** Microsoft released Zork I, II and III under the MIT licence in 2025. Their story files are in the `COMPILED` folder of [historicalsource/zork1](https://github.com/historicalsource/zork1/tree/master/COMPILED), [zork2](https://github.com/historicalsource/zork2/tree/master/COMPILED) and [zork3](https://github.com/historicalsource/zork3/tree/master/COMPILED).
- **Tested and playing:** Zork I, II and III, Deadline, Starcross, Suspended, The Witness, Planetfall, Enchanter, Infidel, Sorcerer, Seastalker, Cutthroats, The Hitchhiker's Guide to the Galaxy, Suspect, Wishbringer, Spellbreaker, Ballyhoo, Leather Goddesses of Phobos, Moonmist, Hollywood Hijinx, Stationfall, The Lurking Horror and Plundered Hearts. As far as we know, that's every Infocom game made in version 3. Each one loads, plays, saves and restores, and shows up under its proper name.
- To load a game, drag the file onto the page, or use **Options → Story file → Load .z3**.
- The game stays loaded next time you visit. **Reset** on the top bar takes the disk out and drops you back at the machine's own prompt or desktop. Your place in the game is kept.
- Each game keeps its own saves and auto-resume. Take a game out and load it again later, and its saves are still there.
- The file stays in your browser. Nothing is uploaded anywhere.

## Features

- **The real games:** a Z-machine interpreter written for this project runs the original story files.
- **Saving:** type `SAVE` or `RESTORE` and pick a position from 1 to 5. The **Saves** panel can load, export and import positions. Exports are standard Quetzal files that other Z-machine interpreters, such as Frotz, can open.
- **Auto-resume:** close the page and you pick up where you left off.
- **Transcripts:** **Saves → Save transcript** downloads your whole game as a text file.
- **Boot sequences:** each machine starts up the way it used to, and waits at its own prompt or desktop until you give it a disk. Start-ups play once per visit. Turn them off in **Options → Nostalgia**.
- **Resizable windows** on the Macintosh, Amiga and NeXTSTEP desktops, remembered per machine.
- **Reset, restart and factory reset:** **Reset** on the top bar ejects the disk. In **Options → Machine**, Restart reboots with the same disk and starts the story over, and Factory reset clears disks, saves and settings (both ask you to click twice).
- **Options:** sound effects, CRT scanlines, amber or green IBM phosphor, an Apple II 80-column card, and a fixed random seed for repeatable games.

Saves, auto-resume and the story files you load are stored in your browser only. Use **Export** to keep a copy of a save.

## Which Zork I?

The `zork1.z3` in Microsoft's release is **Release 119 / Serial 880429**, the final development build preserved in Infocom's archive. It is not the Release 88 that shipped on disk, so a few messages and details differ from the version you may remember. The Zork II and III files are likewise late builds (Release 63 and Release 25). If you have the shipped story files, they load just the same.

## Limitations

- Plays **version 3** story files only. Later Infocom games such as *Trinity*, *A Mind Forever Voyaging* or the graphical ones use newer formats and will not run.
- The C64 and Apple II prompts need a keyboard; on a phone, use the buttons on screen.
- Fonts load from Google Fonts when online. Offline, each machine falls back to a built-in font.

## Source code

`index.html` is packed small. The same code, laid out for reading, is in [`z3-multiboot-readable.html`](z3-multiboot-readable.html), which also plays if you open it.

To rebuild `index.html` from the readable file:

```
python3 build.py
```

It uses Zopfli for the smallest file if installed (`pip install zopfli`) and plain gzip if not. The published `index.html` was made exactly this way.

The Welcome Disk, *The Computer Room*, is written in Inform 6 with the [PunyInform](https://github.com/johanberntsson/PunyInform) library. Its source is [`welcome.inf`](welcome.inf), and the compiled disk is [`the-computer-room.z3`](the-computer-room.z3) if you want to play it in Frotz or another Z-machine player. It has its own release numbers, separate from the player's version. To change it, compile it to version 3 and put the new disk into the readable file:

```
inform6 -v3 +include_path=PunyInform/lib welcome.inf welcome.z3
python3 build.py --welcome welcome.z3
```

## Version history

- **0.5** (November 2026): renamed **Z3 Multiboot**. Bring your own disk: no game is built in any more; drop any version 3 story file on the page. New Welcome Disk adventure (The Computer Room, Release 2). Software on every machine: C64 BASIC, Apple II ELIZA and LEDGER ][, the Amiga Workbench and DH0: hard drive. Reset button, Restart computer and Factory reset. Boot sequences, saves kept per game, built-in unpacker so the page runs in more browsers, readable source and build script. Positions saved in 0.4 still load when you drop in Microsoft's `zork1.z3`.
- **0.4** (November 2026): first public release, as *Zork: The Retro Edition*, with Zork I built in.

## Credits

- **Infocom** for the Z-machine and the games it ran. **Microsoft** released Zork I, II and III under the MIT licence in 2025 (published at [historicalsource](https://github.com/historicalsource)). No game files are included here.
- **Welcome Disk** written by Mark Dowling, compiled with [Inform 6](https://github.com/DavidKinder/Inform6) and the [PunyInform](https://github.com/johanberntsson/PunyInform) library by Fredrik Ramsberg and Johan Berntsson (MIT licence).
- **ELIZA** is our own take on Joseph Weizenbaum's 1966 program, with our own script.
- **Boing!** is remade in tribute to the 1984 Amiga demo by Dale Luck and RJ Mical.
- **Fonts:** IBM Plex, Press Start 2P, VT323 and Sixtyfour, via Google Fonts (SIL Open Font Licence).
- **Developed by Mark Dowling**, Berwick, Melbourne, Australia, November 2026. Built with Claude, with ChatGPT on the initial spec and quality checks, and the name suggested by Gemini.

## Licence

- **No game story files are included.** Games you load are yours to source and look after; Z3 Multiboot just plays them.
- **Z3 Multiboot** (the player, machine designs, extras and the Welcome Disk) was created by Mark Dowling and is **released into the public domain**: see [`LICENSE`](LICENSE). Copy it, change it, remix it, no permission needed. A credit is appreciated if you share your own version.
- **PunyInform**, compiled into the Welcome Disk, is © 2019 Fredrik Ramsberg and Johan Berntsson and keeps its own MIT licence; the full notice is in the comments at the top of `index.html`.
- Game and computer names are trademarks of their owners and are not covered by the above.
