#!/usr/bin/env sh
set -e
#LOG=/home/ecoluo/caffe/examples/tinyimagenet_luot/log/record-'date +%Y-%m-%d-%H-%M-%S'.log
#-snapshot /home/ecoluo/caffe/examples/tinyimagenet_luot/models/caffenet_train_iter_22218.solverstate 



NOW=$(date +%Y-%m-%d-%H-%M)
my_current=${PWD##*/}
LOG=/home/ecoluo/caffe/examples/tinyimagenet_luot/process/self_tiny_phase/log/record-at-$my_current-$NOW.log
echo $NOW
echo $LOG

#-snapshot /home/ecoluo/caffe/examples/tinyimagenet_luot/models/caffenet_train_iter_22218.solverstate 

#/home/ecoluo/caffe/build/tools/caffe train --solver=/home/ecoluo/caffe/examples/tinyimagenet_luot/process/solver.prototxt 2>&1 | tee LOG $@ 

/home/ecoluo/caffe/build/tools/caffe train --solver=/home/ecoluo/caffe/examples/tinyimagenet_luot/process/self_tiny_phase/solverself.prototxt 2>&1 | tee $LOG $@ 

