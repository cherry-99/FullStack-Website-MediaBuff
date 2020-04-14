<!DOCTYPE html>
<html lang="zxx">
	<head>
		<title>MediaBuff</title>
		<meta charset="UTF-8">
		<!-- Stylesheets -->
		<link rel="stylesheet" href="../css/bootstrap.min.css"/>
		<link rel="stylesheet" href="../css/font-awesome.min.css"/>
		<link rel="stylesheet" href="../css/elegant-icons.css"/>
		<link rel="stylesheet" href="../css/owl.carousel.min.css"/>
		<link rel="stylesheet" href="../css/NavBar.css"/>
		<link rel="stylesheet" href="../css/search.css"/>

		<!-- Main Stylesheets -->
		<link rel="stylesheet" href="../css/style.css"/>
	</head>
	<body>
        <!-- Page Preloder -->
        <div id="preloder">
            <div class="loader"></div>
        </div>

        <!-- Offcanvas Menu Section -->
	    <div class="offcanvas-menu-wrapper">
		    <div class="menu-header">
			    <a href="../index.html" class="site-logo">
				    <!-- <img src="img/logo.png" alt=""> -->
				    <h3 style="color: darkcyan;">MediaBuff</h3>
			    </a>
			    <div class="menu-switch" id="menu-canvas-close">
				    <i class="icon_close"></i>
			    </div>
		    </div>
		    <ul class="main-menu">
			    <li><a href="../index.html" class="active">Home</a></li>
			    <li><a href="../gallery.html">Movies</a></li>
			    <li><a href="../blog.html">TV Series</a></li>
			    <li><a href="../news.html">News</a></li>
			    <li><a href="../contact.html">Contact</a></li>
		    </ul>
	    </div>
	    <!-- Offcanvas Menu Section end -->
        
        <!-- Header section -->
        <header class="header-section">
            <a href="../index.html" class="site-logo">
                <!-- <img src="img/logo.png" alt=""> -->
                <h3 style="color: darkcyan;">MediaBuff | Movies</h3>
            </a>
        </header>
        <br><br>
        <!-- Header section end -->
        <section class="hero-section">
            <div class="hero-slider owl-carousel">
                <div class="hero-item">
				    <div class="hero-text hello">
						<h3 style="color: royalblue">movie_name</h3><br>
						<h4>
                        <p>Director : movie_director</p>
                        <p>Duration : movie_duration</p>
                        <p>Actor 1 : movie_actor1</p>
                        <p>Actor 2 : movie_actor2</p>
                        <p>Actor 3 : movie_actor3</p>
                        <p>Gross Income in $ : movie_gross_income</p>
                        <p>Genre : movie_genre</p>
                        <p>PEGI : movie_PEGI</p>
                        <p>IMDB Rating : movie_rating</p>
						<a href="movie_IMDB">Visit IMDB page</a>
						</h4>
				    </div>
				    <div class="my-pic set-bg" data-setbg="poster_location"></div>
                </div>
            </div>
        </section>


        <!--====== Javascripts & Jquery ======-->
	    <script src="../js/vendor/jquery-3.2.1.min.js"></script>
	    <script src="../js/bootstrap.min.js"></script>
	    <script src="../js/owl.carousel.min.js"></script>
	    <script src="../js/masonry.pkgd.min.js"></script>
	    <script src="../js/main.js"></script>
</body>
</html>