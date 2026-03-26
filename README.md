# BuildCored-Orcas-Day2
AirCanvas — BUILDCORED ORCAS Day 02

What it does
Computer detects the closeness of thumb and index fingers, then proves it by changing circle colors.

Hardware concept
Computer Vision's role is detecting(locations fingers), while MediaPipe gives coordinates (for fingiers), and NumPy does math calculations(distance of fingers). Distance determines the colors(far - blue; close - yellow)

Screenshot
https://drive.google.com/file/d/1atagSxky-wJIjHb9KRk3BptC4f14e-Tt/view?usp=sharing
https://drive.google.com/file/d/1IopRO0Yr3SEYPlz0vWfIgqY2EnwfsECG/view?usp=sharing

What I would do differently
This concept can be very well used for security purposes, eg, in daily life if something or someone is close to something untouchable, system cab detect it with red color(for example). When red color manifests, a warning music is played(eg, Beep,beep)

Run it
 python day02_starter.py 
