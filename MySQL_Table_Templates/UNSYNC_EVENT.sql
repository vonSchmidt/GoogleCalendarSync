-- phpMyAdmin SQL Dump
-- version 4.2.12deb2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 07, 2015 at 05:55 PM
-- Server version: 5.5.43-0+deb8u1
-- PHP Version: 5.6.7-1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `events`
--

-- --------------------------------------------------------

--
-- Table structure for table `UNSYNC_EVENT`
--

CREATE TABLE IF NOT EXISTS `UNSYNC_EVENT` (
  `EVENTS_PUID` int(11) NOT NULL,
  `OPERATION_MODE` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `UNSYNC_EVENT`
--
ALTER TABLE `UNSYNC_EVENT`
 ADD PRIMARY KEY (`EVENTS_PUID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `UNSYNC_EVENT`
--
ALTER TABLE `UNSYNC_EVENT`
ADD CONSTRAINT `UNSYNC_EVENT_ibfk_1` FOREIGN KEY (`EVENTS_PUID`) REFERENCES `EVENT` (`EVENTS_PUID`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
