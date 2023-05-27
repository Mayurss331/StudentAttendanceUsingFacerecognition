-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 27, 2023 at 08:48 AM
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
-- Table structure for table `asu1tybjava`
--

CREATE TABLE `asu1tybjava` (
  `Date` text NOT NULL,
  `Mayur` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `asu1tybjava`
--

INSERT INTO `asu1tybjava` (`Date`, `Mayur`) VALUES
('27-05-2023', 1);

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
-- Table structure for table `sybsc_stud_info`
--

CREATE TABLE `sybsc_stud_info` (
  `RollNo` int(11) NOT NULL,
  `Name` text NOT NULL,
  `MobileNo` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
(1, 'Mayur', ' 999999999');

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
(1, 'Asur', 'Mayur', '9370840146', 'Male', '01-01-2002', 'Java', 'Asur', 'TyBsc');

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
