-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 30, 2023 at 07:55 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `petiteannoncedb`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbladmin`
--

CREATE TABLE `tbladmin` (
  `admin_id` int(11) NOT NULL,
  `username` varchar(30) NOT NULL,
  `profile` blob NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbladmin`
--

INSERT INTO `tbladmin` (`admin_id`, `username`, `profile`, `email`, `password`) VALUES
(16, 'Tanjiro Kamado', '', 'TanjiroKamado@gmail.com', '12345'),
(17, 'Nezuko Kamado', '', 'NezukoKamado@gmail.com', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `tblcategory`
--

CREATE TABLE `tblcategory` (
  `catid` int(11) NOT NULL,
  `cat_type` varchar(255) NOT NULL,
  `admin_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tblcategory`
--

INSERT INTO `tblcategory` (`catid`, `cat_type`, `admin_id`) VALUES
(11, 'Multimedia', NULL),
(12, 'Home-Furniture', NULL),
(13, 'Home-Kitchen and Bathroom', NULL),
(14, 'leisure', NULL),
(15, 'Home-Maintenance', NULL),
(16, 'Sport', NULL),
(17, 'kids', NULL),
(18, 'pets', NULL),
(25, 'Car Rental', NULL),
(41, 'Service', NULL),
(42, 'Entertainment', NULL),
(49, 'Home Decoration', NULL),
(82, 'Fashion and wellness', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `tbldisctrict`
--

CREATE TABLE `tbldisctrict` (
  `loc_id` int(11) NOT NULL,
  `district` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbldisctrict`
--

INSERT INTO `tbldisctrict` (`loc_id`, `district`) VALUES
(1, 'flacq'),
(3, 'Rivere du Rempart'),
(4, 'Black River'),
(5, 'Grand Port'),
(6, 'Triolet'),
(7, 'Pamplemousse'),
(8, 'Quatre Bornes'),
(9, 'Savanne'),
(10, 'Rose Hill'),
(11, 'Port Louis'),
(12, 'Moka');

-- --------------------------------------------------------

--
-- Table structure for table `tblfavourite`
--

CREATE TABLE `tblfavourite` (
  `f_id` int(11) NOT NULL,
  `p_id` int(11) DEFAULT NULL,
  `id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tblfavourite`
--

INSERT INTO `tblfavourite` (`f_id`, `p_id`, `id`) VALUES
(11, 36, 43),
(12, 37, 47);

-- --------------------------------------------------------

--
-- Table structure for table `tblfavourite_service`
--

CREATE TABLE `tblfavourite_service` (
  `offer_id` int(11) NOT NULL,
  `userid` int(11) DEFAULT NULL,
  `s_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tblfavourite_service`
--

INSERT INTO `tblfavourite_service` (`offer_id`, `userid`, `s_id`) VALUES
(41, 43, 25),
(44, 47, 27);

-- --------------------------------------------------------

--
-- Table structure for table `tbloffer`
--

CREATE TABLE `tbloffer` (
  `offerid` int(11) NOT NULL,
  `userid` int(11) DEFAULT NULL,
  `message` varchar(255) NOT NULL,
  `amount` float NOT NULL,
  `product_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbloffer`
--

INSERT INTO `tbloffer` (`offerid`, `userid`, `message`, `amount`, `product_id`) VALUES
(2, 43, 'could you reduce the price', 200, 42),
(4, 47, 'I want this lamp', 200, 37);

-- --------------------------------------------------------

--
-- Table structure for table `tbloffer_service`
--

CREATE TABLE `tbloffer_service` (
  `offer_id` int(11) NOT NULL,
  `message` varchar(255) NOT NULL,
  `amount` float NOT NULL,
  `userid` int(11) DEFAULT NULL,
  `s_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbloffer_service`
--

INSERT INTO `tbloffer_service` (`offer_id`, `message`, `amount`, `userid`, `s_id`) VALUES
(1, 'aa', 2000, 43, 25),
(2, 'rrrrrrrrrrr', 2000, 43, 25),
(3, 'aaaa', 2900, 43, 25),
(4, 'aaaaaaa', 2000, 43, 25),
(5, 'aaaa', 4000, 43, 25),
(6, 'qqqqqqqqqqq', 1200, 43, 25),
(7, 'aaaaaa', 2000, 43, 25),
(8, 'aaaaaa', 2000, 43, 25),
(9, 'aaaaaa', 2000, 43, 25),
(10, 'aaaaaa', 2000, 43, 25),
(11, 'aaaaaa', 2000, 43, 25),
(12, 'aaaaaa', 2000, 43, 25),
(13, 'aaaaaa', 2000, 43, 25),
(14, 'aaaaaa', 2000, 43, 25),
(15, 'aaaaaa', 2000, 43, 25),
(16, 'aaaaaa', 2000, 43, 25),
(17, 'aaaaaa', 2000, 43, 25),
(18, 'aaaaaa', 2000, 43, 25),
(19, 'aaaaaa', 2000, 43, 25),
(20, 'aaaaaa', 2000, 43, 25),
(21, 'aaaaaa', 2000, 43, 25),
(22, 'aaaaaa', 2000, 43, 25),
(23, 'aaaaaa', 2000, 43, 25),
(24, 'aaaaaa', 2000, 43, 25),
(25, 'aaaaaa', 2000, 43, 25),
(26, 'aaaaaa', 2000, 43, 25),
(27, 'aaaaaa', 2000, 43, 25),
(28, 'aaaaaa', 2000, 43, 25),
(29, 'aaaaaa', 2000, 43, 25),
(30, 'aaaaaa', 2000, 43, 25),
(31, 'aaaaaa', 2000, 43, 25),
(32, 'aaaaaa', 2000, 43, 25),
(33, 'aaaaaa', 2000, 43, 25),
(34, 'aaaaaa', 2000, 43, 25),
(35, 'aaaaaa', 2000, 43, 25),
(36, 'aaaaaa', 2000, 43, 25),
(37, 'aaaaaa', 2000, 43, 25),
(38, 'aaaaaa', 2000, 43, 25),
(39, 'aaaaaa', 2000, 43, 25),
(40, 'aaaaaa', 2000, 43, 25),
(41, 'aaaaaa', 2000, 43, 25),
(42, 'aaaaaa', 2000, 43, 25),
(43, 'aaaaaa', 2000, 43, 25),
(44, 'aa', 400, 43, 25),
(46, 'Could you reduce the price', 200, 43, 27);

-- --------------------------------------------------------

--
-- Table structure for table `tblphotogal`
--

CREATE TABLE `tblphotogal` (
  `gallery-id` int(11) NOT NULL,
  `photo_data` blob NOT NULL,
  `product_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tblproduct_advert`
--

CREATE TABLE `tblproduct_advert` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `descr` varchar(255) NOT NULL,
  `price` int(11) NOT NULL,
  `usage_time` int(11) NOT NULL,
  `document` varchar(255) NOT NULL,
  `expiry_date` date NOT NULL,
  `status` varchar(11) NOT NULL DEFAULT 'pending',
  `renew` int(11) NOT NULL DEFAULT 0,
  `request` int(11) NOT NULL DEFAULT 0,
  `cat_id` int(11) DEFAULT NULL,
  `id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tblproduct_advert`
--

INSERT INTO `tblproduct_advert` (`product_id`, `product_name`, `descr`, `price`, `usage_time`, `document`, `expiry_date`, `status`, `renew`, `request`, `cat_id`, `id`) VALUES
(32, 'Nins', 'Keep yourself away from diseases', 350, 2, '/static/images\\nins.jpg', '2023-08-04', 'Approve', 1, 1, 14, 45),
(33, 'lucozade', 'freshing drink and keep you energies', 500, 5, '/static/images\\luu.jpg', '2023-08-04', 'pending', 0, 0, 16, 45),
(35, 'Gamingnotebook', 'Game with style and better performance ', 200000, 5, '/static/images\\laptop.gif', '2023-08-05', 'Approve', 0, 0, 11, 45),
(36, 'Iphone 13', 'High resolution camera', 120000, 7, '/static/images\\phone.gif', '2023-08-05', 'Approve', 0, 0, 11, 43),
(37, 'Lava Lamp', 'Keep your living room elegant and beautiful', 350, 4, '/static/images\\lamp.gif', '2023-08-05', 'Approve', 0, 0, 12, 45),
(38, 'Gamer Chair', 'Help you to relax your muscles while gaming', 1200, 5, '/static/images\\chair.gif', '2023-08-05', 'Approve', 0, 0, 12, 45),
(39, 'Air fryer', 'Enjoy healthier versions of your favorite fried ', 5000, 5, '/static/images\\air.gif', '2023-08-05', 'Approve', 0, 0, 13, 43),
(40, 'Cake Mixer', 'Faciliate your life with our new mixer', 400, 5, '/static/images\\mixer.gif', '2023-08-05', 'Approve', 0, 0, 13, 43),
(41, 'Apple Watch', 'Keep it classic and trendy', 1200, 6, '/static/images\\watch.gif', '2023-08-05', 'Approve', 0, 0, 14, 43),
(42, 'Perfume', 'Alcohol free perfume', 1000, 4, '/static/images\\perfum.gif', '2023-08-05', 'Approve', 0, 0, 14, 43),
(43, 'Drill Machine', 'Faciliate your life with maintaining', 300, 5, '/static/images\\drill.gif', '2023-08-05', 'Approve', 0, 0, 15, 43),
(44, 'ChainSaw', 'Faciliate your life with maintaining', 350, 6, '/static/images\\chain.gif', '2023-08-05', 'Approve', 0, 0, 15, 43),
(45, 'Sport Shoes', '1200', 2000, 5, '/static/images\\SHOES.gif', '2023-08-05', 'Approve', 0, 0, 16, 43),
(46, 'Volleyball', 'Strong ball', 200, 6, '/static/images\\volley.gif', '2023-08-05', 'Approve', 0, 0, 16, 43),
(47, 'Toy Gun', 'High quality toy', 350, 6, '/static/images\\gun.gif', '2023-08-05', 'Approve', 0, 0, 17, 43),
(48, 'Monster Toy', 'High quality toy', 350, 6, '/static/images\\toy.gif', '2023-08-05', 'Approve', 0, 0, 17, 43),
(49, 'Leash', 'Faciliate time with the dog', 350, 6, '/static/images\\dog.gif', '2023-08-05', 'Approve', 0, 0, 18, 43),
(50, 'Dog Treat', 'Tasty snack for your dogs', 350, 5, '/static/images\\treats.gif', '2023-08-05', 'Approve', 0, 0, 18, 45),
(51, 'Rented bmw', 'Rent cars for special occasions  per hour', 250, 5, '/static/images\\car.gif', '2023-08-05', 'Approve', 0, 0, 25, 45),
(52, 'HeadSet', 'Be trendy', 1200, 6, '/static/images\\headset.gif', '2023-08-05', 'Approve', 0, 0, 42, 43),
(53, 'Earbud', 'Be trendy', 1200, 6, '/static/images\\earbuds.gif', '2023-08-05', 'Approve', 0, 0, 42, 43),
(54, 'Vase', 'Make your living room beautifull', 350, 6, '/static/images\\vase.gif', '2023-08-05', 'Approve', 0, 0, 49, 43),
(55, 'Scented Candle', 'Make a pleasant environment', 350, 6, '/static/images\\candle.gif', '2023-08-05', 'Approve', 0, 0, 49, 43),
(56, 'Lipstick', 'Keep your health nice and shiney', 350, 5, '\\static\\images\\lips.jpg', '2023-08-06', 'Approve', 0, 0, 82, 47);

-- --------------------------------------------------------

--
-- Table structure for table `tblreviews`
--

CREATE TABLE `tblreviews` (
  `review_id` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `r_details` varchar(255) NOT NULL,
  `id` int(11) DEFAULT NULL,
  `s_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tblservice_advert`
--

CREATE TABLE `tblservice_advert` (
  `s_id` int(11) NOT NULL,
  `service_name` varchar(25) NOT NULL,
  `descr` varchar(255) NOT NULL,
  `document` varchar(255) NOT NULL,
  `expiry_date` date NOT NULL,
  `status` varchar(10) NOT NULL DEFAULT 'pending',
  `renew` int(11) NOT NULL DEFAULT 0,
  `request` int(11) NOT NULL DEFAULT 0,
  `cat_id` int(11) DEFAULT NULL,
  `id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tblservice_advert`
--

INSERT INTO `tblservice_advert` (`s_id`, `service_name`, `descr`, `document`, `expiry_date`, `status`, `renew`, `request`, `cat_id`, `id`) VALUES
(18, 'Manicure', 'Relax and unwind with our comfortable hammock.', '/static/images\\download (2).jpg', '2023-08-05', 'Reject', 1, 1, 41, 43),
(21, 'Air Fryer', 'Enjoy healthier versions of your favorite fried ', 'webappfiles\\static\\images\\download (1).jpg', '2023-07-30', 'pending', 0, 0, 41, 43),
(23, 'aa', 'aaaaa', '\\static\\images\\download (1).jpg', '2023-07-30', 'pending', 0, 0, 41, 43),
(25, 'Gift wrapping', 'Wrap your gifts with our high quality papers', '\\static\\images\\download (3).jpg', '2023-08-01', 'Approve', 0, 0, 41, 43),
(26, 'Manicure', 'Enjoy healthier versions of your favorite fried ', '\\static\\images\\air fryer.jpg', '2023-08-03', 'pending', 0, 0, 41, 43),
(27, 'Hair Styling', 'Keep your health nice and shiney', '\\static\\images\\hait.jpg', '2023-08-04', 'Approve', 0, 0, 41, 45),
(28, 'Dry Cleaning', 'Keep your clothes shiny and clean', '\\static\\images\\dry.jpg', '2023-08-04', 'Approve', 0, 0, 41, 45),
(29, 'Gift Wrapping', 'Good quality wraping', '\\static\\images\\download (3).jpg', '2023-08-05', 'Approve', 0, 0, 41, 43),
(30, 'Plumbing', 'Repair all your problems in an instant', '\\static\\images\\download (7).jpg', '2023-08-05', 'Approve', 0, 0, 41, 45);

-- --------------------------------------------------------

--
-- Table structure for table `tbltestimonial`
--

CREATE TABLE `tbltestimonial` (
  `test_id` int(11) NOT NULL,
  `t_details` varchar(255) NOT NULL,
  `userid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbltestimonial`
--

INSERT INTO `tbltestimonial` (`test_id`, `t_details`, `userid`) VALUES
(1, 'It is the best website for buying and selling', 43),
(5, 'User friendly website', 45),
(6, 'I love this website', 18);

-- --------------------------------------------------------

--
-- Table structure for table `tbluser`
--

CREATE TABLE `tbluser` (
  `id` int(11) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `username` varchar(40) NOT NULL,
  `gender` varchar(30) NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  `frozen` varchar(11) NOT NULL DEFAULT 'Active',
  `password` varchar(255) NOT NULL,
  `loc_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbluser`
--

INSERT INTO `tbluser` (`id`, `lname`, `fname`, `email`, `username`, `gender`, `phone_number`, `frozen`, `password`, `loc_id`) VALUES
(18, 'Hisoka ', 'Morow', 'HisokaMorow@gmail.com', 'Hisoka Morow', 'male', '56123456', 'inactive', '234565', 5),
(20, 'Joseph ', 'Joestar', 'JosephJoestar@gmail.com', 'Joseph Joestar', 'male', '53451234', 'active', '22233', 7),
(21, 'Kakashi ', 'Hatake', 'KakashiHatake@gmail.com', 'Kakashi Hatake', 'male', '54123456', 'active', '1dd24d3', 9),
(22, 'Satoru ', 'Gojo', 'SatoruGojo@gmail.com', 'Satoru Gojo', 'male', '5312458', 'active', 'w2e212', 4),
(23, 'Itachi ', 'Uchiha', 'ItachiUchiha@gmail', 'Itachi Uchiha', 'female', '52345698', 'inactive', '12345', 11),
(25, 'Light ', 'Yagami', 'LightYagami@gmail', 'Light Yagami', 'male', '541234', 'active', 'd34f4', 10),
(43, 'Alasoo', 'Adrien', 'darrenalassoo@gmail.com', 'Adrien Alasoo', 'male', '512334', 'active', '123456', 3),
(45, 'Chenning', 'Chen', 'tahseenneerooa11@gmail.com', 'Chenn', 'female', '57123456', 'active', '123456', NULL),
(47, 'Evergarder', 'Yanah', 'yanyanah2212@gmail.com', 'yanah', 'female', '5915174', 'active', 'juice', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbladmin`
--
ALTER TABLE `tbladmin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `tblcategory`
--
ALTER TABLE `tblcategory`
  ADD PRIMARY KEY (`catid`),
  ADD KEY `fk_admin_id` (`admin_id`);

--
-- Indexes for table `tbldisctrict`
--
ALTER TABLE `tbldisctrict`
  ADD PRIMARY KEY (`loc_id`);

--
-- Indexes for table `tblfavourite`
--
ALTER TABLE `tblfavourite`
  ADD PRIMARY KEY (`f_id`),
  ADD KEY `fk_p_iddd` (`p_id`),
  ADD KEY `fkk_idddd` (`id`);

--
-- Indexes for table `tblfavourite_service`
--
ALTER TABLE `tblfavourite_service`
  ADD PRIMARY KEY (`offer_id`),
  ADD KEY `iddd` (`userid`),
  ADD KEY `s_idddddddddd` (`s_id`);

--
-- Indexes for table `tbloffer`
--
ALTER TABLE `tbloffer`
  ADD PRIMARY KEY (`offerid`),
  ADD KEY `fk_user_offer` (`userid`),
  ADD KEY `fk_product_id` (`product_id`);

--
-- Indexes for table `tbloffer_service`
--
ALTER TABLE `tbloffer_service`
  ADD PRIMARY KEY (`offer_id`),
  ADD KEY `fkkkkkkiddd` (`userid`),
  ADD KEY `fkkkkkkkksid` (`s_id`);

--
-- Indexes for table `tblphotogal`
--
ALTER TABLE `tblphotogal`
  ADD PRIMARY KEY (`gallery-id`),
  ADD KEY `fk_photo_advert_id` (`product_id`);

--
-- Indexes for table `tblproduct_advert`
--
ALTER TABLE `tblproduct_advert`
  ADD PRIMARY KEY (`product_id`),
  ADD KEY `fk_cat_idd` (`cat_id`),
  ADD KEY `fk_iddd` (`id`);

--
-- Indexes for table `tblreviews`
--
ALTER TABLE `tblreviews`
  ADD PRIMARY KEY (`review_id`),
  ADD KEY `fk_user_review_id` (`id`),
  ADD KEY `fk_usere_serv_ad` (`s_id`);

--
-- Indexes for table `tblservice_advert`
--
ALTER TABLE `tblservice_advert`
  ADD PRIMARY KEY (`s_id`),
  ADD KEY `fk_user_id_serv` (`cat_id`),
  ADD KEY `fkkk_idddd` (`id`);

--
-- Indexes for table `tbltestimonial`
--
ALTER TABLE `tbltestimonial`
  ADD PRIMARY KEY (`test_id`),
  ADD KEY `fk_user_id_test` (`userid`);

--
-- Indexes for table `tbluser`
--
ALTER TABLE `tbluser`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_loc_id` (`loc_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbladmin`
--
ALTER TABLE `tbladmin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `tblcategory`
--
ALTER TABLE `tblcategory`
  MODIFY `catid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84;

--
-- AUTO_INCREMENT for table `tbldisctrict`
--
ALTER TABLE `tbldisctrict`
  MODIFY `loc_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `tblfavourite`
--
ALTER TABLE `tblfavourite`
  MODIFY `f_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `tblfavourite_service`
--
ALTER TABLE `tblfavourite_service`
  MODIFY `offer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `tbloffer`
--
ALTER TABLE `tbloffer`
  MODIFY `offerid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tbloffer_service`
--
ALTER TABLE `tbloffer_service`
  MODIFY `offer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT for table `tblphotogal`
--
ALTER TABLE `tblphotogal`
  MODIFY `gallery-id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tblproduct_advert`
--
ALTER TABLE `tblproduct_advert`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `tblreviews`
--
ALTER TABLE `tblreviews`
  MODIFY `review_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tblservice_advert`
--
ALTER TABLE `tblservice_advert`
  MODIFY `s_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `tbltestimonial`
--
ALTER TABLE `tbltestimonial`
  MODIFY `test_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tbluser`
--
ALTER TABLE `tbluser`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tblcategory`
--
ALTER TABLE `tblcategory`
  ADD CONSTRAINT `fk_admin_id` FOREIGN KEY (`admin_id`) REFERENCES `tbladmin` (`admin_id`) ON DELETE CASCADE;

--
-- Constraints for table `tblfavourite`
--
ALTER TABLE `tblfavourite`
  ADD CONSTRAINT `fk_p_iddd` FOREIGN KEY (`p_id`) REFERENCES `tblproduct_advert` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fkk_idddd` FOREIGN KEY (`id`) REFERENCES `tbluser` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tblfavourite_service`
--
ALTER TABLE `tblfavourite_service`
  ADD CONSTRAINT `iddd` FOREIGN KEY (`userid`) REFERENCES `tbluser` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `s_idddddddddd` FOREIGN KEY (`s_id`) REFERENCES `tblservice_advert` (`s_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tbloffer`
--
ALTER TABLE `tbloffer`
  ADD CONSTRAINT `fk_product_id` FOREIGN KEY (`product_id`) REFERENCES `tblproduct_advert` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_user_offer` FOREIGN KEY (`userid`) REFERENCES `tbluser` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tbloffer_service`
--
ALTER TABLE `tbloffer_service`
  ADD CONSTRAINT `fkkkkkkiddd` FOREIGN KEY (`userid`) REFERENCES `tbluser` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fkkkkkkkksid` FOREIGN KEY (`s_id`) REFERENCES `tblservice_advert` (`s_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tblphotogal`
--
ALTER TABLE `tblphotogal`
  ADD CONSTRAINT `fk_p_id` FOREIGN KEY (`product_id`) REFERENCES `tblproduct_advert` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tblproduct_advert`
--
ALTER TABLE `tblproduct_advert`
  ADD CONSTRAINT `fk_cat_idd` FOREIGN KEY (`cat_id`) REFERENCES `tblcategory` (`catid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_iddd` FOREIGN KEY (`id`) REFERENCES `tbluser` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tblreviews`
--
ALTER TABLE `tblreviews`
  ADD CONSTRAINT `fk_user_review_id` FOREIGN KEY (`id`) REFERENCES `tbluser` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_usere_serv_ad` FOREIGN KEY (`s_id`) REFERENCES `tblservice_advert` (`s_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tblservice_advert`
--
ALTER TABLE `tblservice_advert`
  ADD CONSTRAINT `fk_cat_iddd` FOREIGN KEY (`cat_id`) REFERENCES `tblcategory` (`catid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fkkk_idddd` FOREIGN KEY (`id`) REFERENCES `tbluser` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tbltestimonial`
--
ALTER TABLE `tbltestimonial`
  ADD CONSTRAINT `fk_user_id_test` FOREIGN KEY (`userid`) REFERENCES `tbluser` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tbluser`
--
ALTER TABLE `tbluser`
  ADD CONSTRAINT `fk_loc_id` FOREIGN KEY (`loc_id`) REFERENCES `tbldisctrict` (`loc_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
