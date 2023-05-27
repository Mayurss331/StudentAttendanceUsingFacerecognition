-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 27, 2023 at 01:06 PM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.2.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `attendence`
--

-- --------------------------------------------------------

--
-- Table structure for table `attend`
--

CREATE TABLE `attend` (
  `Date` text NOT NULL,
  `Mayur` int(11) NOT NULL,
  `Ruchika` int(11) NOT NULL,
  `Yogita` int(10) NOT NULL,
  `Jayeshree` int(10) NOT NULL,
  `swapnali` int(10) NOT NULL,
  `Lina` int(10) NOT NULL,
  `tejashree` int(10) NOT NULL,
  `Pushkar` int(10) NOT NULL,
  `Vrushali` int(10) NOT NULL,
  `Shubhangi` int(10) NOT NULL,
  `Rohit` int(10) NOT NULL,
  `Bhagu` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `attend`
--

INSERT INTO `attend` (`Date`, `Mayur`, `Ruchika`, `Yogita`, `Jayeshree`, `swapnali`, `Lina`, `tejashree`, `Pushkar`, `Vrushali`, `Shubhangi`, `Rohit`, `Bhagu`) VALUES
('25-03-2023', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `fybsc_stud_info`
--

CREATE TABLE `fybsc_stud_info` (
  `RollNo` int(11) NOT NULL,
  `Name` text NOT NULL,
  `MobileNo` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `may1tybjava`
--

CREATE TABLE `may1tybjava` (
  `Date` text,
  `Mayur` int(11) DEFAULT NULL,
  `Ruchika` int(11) DEFAULT NULL,
  `Yogita` int(11) DEFAULT NULL,
  `Jayeshree` int(11) DEFAULT NULL,
  `swapnali` int(11) DEFAULT NULL,
  `Lina` int(11) DEFAULT NULL,
  `tejashree` int(11) DEFAULT NULL,
  `Pushkar` int(11) DEFAULT NULL,
  `Shubhangi` int(11) DEFAULT NULL,
  `Vrushali` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `may1tybjava`
--

INSERT INTO `may1tybjava` (`Date`, `Mayur`, `Ruchika`, `Yogita`, `Jayeshree`, `swapnali`, `Lina`, `tejashree`, `Pushkar`, `Shubhangi`, `Vrushali`) VALUES
('27-03-2023', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `roh2sybpython`
--

CREATE TABLE `roh2sybpython` (
  `Date` text,
  `Rohit` int(11) NOT NULL,
  `Bhagu` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `shu3sybds`
--

CREATE TABLE `shu3sybds` (
  `Date` text,
  `Rohit` int(11) DEFAULT NULL,
  `Bhagu` int(11) DEFAULT NULL,
  `Milind` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `shu3sybds`
--

INSERT INTO `shu3sybds` (`Date`, `Rohit`, `Bhagu`, `Milind`) VALUES
('09-03-2023', 0, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `swp4sybos`
--

CREATE TABLE `swp4sybos` (
  `Date` text,
  `Rohit` int(11) DEFAULT NULL,
  `Bhagu` int(11) DEFAULT NULL,
  `Milind` int(11) DEFAULT NULL,
  `Jayashri` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `swp4sybos`
--

INSERT INTO `swp4sybos` (`Date`, `Rohit`, `Bhagu`, `Milind`, `Jayashri`) VALUES
('30-03-2023', 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `sybsc_stud_info`
--

CREATE TABLE `sybsc_stud_info` (
  `RollNo` int(11) NOT NULL,
  `Name` text NOT NULL,
  `MobileNo` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sybsc_stud_info`
--

INSERT INTO `sybsc_stud_info` (`RollNo`, `Name`, `MobileNo`) VALUES
(1, 'Rohit', '9309802332'),
(2, 'Bhagu', '9809890989'),
(3, 'Milind', ' 945432147'),
(4, 'Jayashri', ' 123456789');

-- --------------------------------------------------------

--
-- Table structure for table `tybsc_stud_info`
--

CREATE TABLE `tybsc_stud_info` (
  `RollNo` int(11) NOT NULL,
  `Name` text NOT NULL,
  `MobileNo` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tybsc_stud_info`
--

INSERT INTO `tybsc_stud_info` (`RollNo`, `Name`, `MobileNo`) VALUES
(1, 'Mayur', '9370840146'),
(2, 'Ruchika', '7620146176'),
(3, 'Yogita', '9999999999'),
(4, 'Jayeshree', ' 888888888'),
(5, 'swapnali', ' 942222206'),
(6, 'Lina', '8888888888'),
(7, 'tejashree', '5555555555'),
(8, 'Pushkar', ' 890890890'),
(9, 'Shubhangi', '8989898989'),
(10, 'Vrushali', '9879879878');

-- --------------------------------------------------------

--
-- Table structure for table `user_data`
--

CREATE TABLE `user_data` (
  `ID` int(11) NOT NULL,
  `Name` text NOT NULL,
  `Email` varchar(50) NOT NULL,
  `MobileNo` varchar(10) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `DoB` varchar(10) NOT NULL,
  `Subject` varchar(20) NOT NULL,
  `Password` varchar(12) NOT NULL,
  `ClassName` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_data`
--

INSERT INTO `user_data` (`ID`, `Name`, `Email`, `MobileNo`, `Gender`, `DoB`, `Subject`, `Password`, `ClassName`) VALUES
(1, 'Mayur Sanjay Sonar', 'Mayur', '9370840146', 'Male', '31-10-2002', 'Java', 'Asur', 'TyBSc'),
(2, 'Rohit', 'r@g.c', '9876543210', 'Male', '20-10-2010', 'Python', 'Rohit@123', 'SyBSc'),
(3, 'Shubhangi', 'aaaaa@gmail.com', '1234567890', 'Female', '25-03-2010', 'DS', 'Aaaaaa@1', 'SyBSc'),
(4, 'swpnali', 'bbbbbb@gmail.com', '1234567899', 'Female', '05-10-2010', 'OS', 'Bbbbbb@1', 'SyBSc');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fybsc_stud_info`
--
ALTER TABLE `fybsc_stud_info`
  ADD PRIMARY KEY (`RollNo`);

--
-- Indexes for table `sybsc_stud_info`
--
ALTER TABLE `sybsc_stud_info`
  ADD PRIMARY KEY (`RollNo`);

--
-- Indexes for table `tybsc_stud_info`
--
ALTER TABLE `tybsc_stud_info`
  ADD PRIMARY KEY (`RollNo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
