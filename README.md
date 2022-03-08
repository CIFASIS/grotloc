# GroTLoc
**Ground Truth for Loop Closure** (**GroTLoC**) is a tool that allows users to easily annotate Datasets with Ground Truth for Loop Detection (LGT) and Loop Closure based on previously obtained Positional Ground Truth (PGT).

---
## Acronyms and Abbreviations

**SLAM**: Simultaneous Localization and Mapping.

**LC**: Loop Closure.

**GT**: Ground Truth.

**LGT**: Loop Closure Ground Truth; a ground truth of poses and expected loop closures for a robot or system.

**PGT**: Positional Ground Truth; a ground truth in terms of poses of the robot or system.

**GroTLoC**: **Gro**und **T**ruth for **Lo**op **C**losure; the name of the tool in this repository.

---
## Problem Statement
In mobile robotics, the problem of Loop Closure encompasses detecting when a mobile robot finds itself transiting an area previously visited and using such information to adjutst the trajectory and estimated map of the robot.
It's a fundamental step on solving the SLAM problem by reducing the robot's accumulated drift.

In the literature you can find many LC systems based on different sources of information (cameras, laser sensors, proprioceptive sensors), and these systems need to be tested against known paths with known loop closures, what we call Loop Closure Gound Truth.

One existing, and very utilized, method for testing a LC system include testing an entire SLAM ,system where LC is just a part of it, by comparing the expected GT pathing taken by the robot with the path computed by the SLAM system. This method is prone to displaying composition issues, that is, issues where the overall SLAM system elected negatively affects the results obtained for the LC system.

To test the LC system on it's own we need a dataset annotated with LGT, that is, a robot or system dataset composed of PGT and annotated with the expected points where the LC is possible.
There are no existing tools to aid with this annotation, as far as we know, so in the literature is common to find datasets manually annotated or annotated with poorly choosen metrics, such as simple euclidian distance between robot poses.

GroTLoC allows to input a PGT, and by choosing or defining the metrics with wich to compare these poses according to the LC method or the robot/system's configuration, generate a LGT.

---
## How to Use

### Input as Pose Ground Truth
The input file represents the PGT of the robot or system from the dataset to analyze.

Currently the tool accepts inputs of the following formats
- [TUM Ground-truth trajectories](https://vision.in.tum.de/data/datasets/rgbd-dataset/file_formats): space-separated values, plaintext file with values '`timestamp tx ty tz qx qy qz qw`'

### Distance Functions


### Manual review and Output
TBD

---
## References
TBD

---
## Milestones

### Input
- [x] "TUM" Input Format
- [ ] "KITTI" Input Format
- [ ] "EuRoC MAV" Input Format

### Distance
- [ ] Implement "Euclidian" distance function
- [ ] Implement "Spherical Linear Interpolation" distance function
- [ ] Implement "Great Circle" distance function
- [ ] Implement "Angular" distance function
- [ ] Outline distance function limitations

### Data Structure
- [ ] Merge into single data structure
- [ ] Describe data structure query complexity

### Manual Review
- [x] Rosbag approximate image retrieval
- [ ] RANSAC Homography calculation