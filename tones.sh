#!/bin/bash

PLAY="/usr/bin/play -q -n"

case "$1" in
	0)
	$PLAY synth pl E2 pl A2 pl D3 pl G3 pl B3 pl E4 delay 0 .05 .1 .15 .2 .25 \
	remix - fade 0 4 .1 norm -1 gain 3 repeat 99 &
	;;
	1)
	$PLAY -c 2 synth 8 sine 30-120 fade 0 0 0.1 repeat 99 &
	;;
	2)
	$PLAY -c 2 synth 8 sine 100-2000 repeat 99 &
	;;
	3)
	$PLAY -c 2 synth 8 sine 30-20000 repeat 99 &
	;;
	4)
	$PLAY -c 2 synth sine 60 &
	;;
	5)
	$PLAY -c 2 synth sine 100 &
	;;
	6)
	$PLAY -c 2 synth sine 500 &
	;;
	7)
	$PLAY -c 2 synth sine 1000 &
	;;
	8)
	$PLAY -c 2 synth whitenoise &
	;;
	9)
	$PLAY -c 2 synth pinknoise &
	;;
esac
