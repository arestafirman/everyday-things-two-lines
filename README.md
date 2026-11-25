# One Cloud, a Million Litres

[![Competition](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/c/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![Rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/arestafirman/everyday-things-two-lines/rank.svg)](https://make.fun/c/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![Reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/arestafirman/everyday-things-two-lines/reward.svg)](https://make.fun/c/u-suga-everyday-things-two-lines-longer-run-f8734479)

## The entry

Rain, pictured as the sky tipping one giant watering can over the whole
street — every roof, leaf, and parked bike gets the same drink at once.
The picture holds for the falling water and the even spread, but it breaks
on scale: a real can holds about two litres, while one storm cloud can drop
a million litres on a single street. The analogy is right about the shape of
the rain and wrong about its size, and that gap is the whole point.

## How it works

`main.py` is plain Python with no dependencies and no network access. It
holds the two lines as constants and writes them, joined by a single
newline and with no trailing newline, to `entry.txt` in the output
directory — `/output` by default, or `$OUTPUT_DIR` when that is set.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The output is exactly 306 characters across two lines.
