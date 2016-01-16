#!/bin/bash

PLAY="/usr/bin/play -q"

case "$1" in
	1)
	$PLAY -n synth pl E2 pl A2 pl D3 pl G3 pl B3 pl E4 delay 0 .05 .1 .15 .2 .25 \
	remix - fade 0 4 .1 norm -1 gain 3 repeat 99 &
	;;
	2)
	$PLAY -n -c 2 synth 8 sine 30-120 fade 0 0 0.1 repeat 99 &
	;;
	3)
	$PLAY -n -c 2 synth 8 sine 100-2000 repeat 99 &
	;;
	4)
	$PLAY -n -c 2 synth 8 sine 30-20000 repeat 99 &
	;;
	5)
	$PLAY -n -c 2 synth sine 60 &
	;;
	6)
	$PLAY -n -c 2 synth sine 100 &
	;;
	7)
	$PLAY -n -c 2 synth sine 500 &
	;;
	8)
	$PLAY -n -c 2 synth sine 1000 &
	;;
	9)
	$PLAY -n -c 2 synth whitenoise &
	;;
	10)
	$PLAY -n -c 2 synth pinknoise &
	;;
	99)
	$PLAY $HOME/EasterEgg.mp3 &
	;;
esac
