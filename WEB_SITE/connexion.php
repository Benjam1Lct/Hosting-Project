<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="Website Icon" type="image/png" href="img/icon2.png">
    <link rel="stylesheet" href="css/header.css">
    <link rel="stylesheet" href="css/login.css">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@3.2.0/fonts/remixicon.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/boxicons@latest/css/boxicons.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600&display=swap" rel="stylesheet">
    <title>SnapOCR</title>
</head>
<body>

    <header>
        <a href="index.html" class="logo"><i class='bx bxs-image-add' ></i><span>SnapOCR</span></a>

        <ul class="navbar">
            <li><a href="index.html" class="active">Home</a></li>
            <li><a href="#" >About Us</a></li>
            <li><a href="#" >Services</a></li>
            <li><a href="#" >Blog</a></li>
            <li class="link-header-signin"><a href="login.html" >Sign in</a></li>
        </ul>

        <div class="main">
            <a href="login.html" class="user"><i class='bx bxs-contact' ></i>Sign In</a>
            <div class="bx bx-menu" id="menu-icon"></div>
        </div>
    </header>

    <div class="container">
        <div class="content">
            <h2 class="icon"><i class='bx bxl-python' undefined ></i>OCR Application</h2>
            <div class="text-sci">
                <h2>Welcome!
                    <br>
                    <span>To Our New Website.</span>
                </h2>    
                <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fuga, quae.</p>
                <div class="social-icons">
                    <a href="#"><i class="ri-facebook-fill"></i></a>
                    <a href="#"><i class="ri-instagram-line"></i></a>
                    <a href="#"><i class="ri-twitter-fill"></i></a>
                    <a href="#"><i class="ri-linkedin-fill"></i></a>
                </div>
            </div>
        </div>
        <div class="logreg-box">

            <div class="form-box login">
                <form id="form-in" action="connexion.php" method="post">
                    <h2>Sign In</h2>

                    <div class="input-box">
                        <span class="icon-input"><i class='bx bxs-envelope' ></i></span>
                        <input type="text" name="email" id="email" required="required" autocomplete="off">
                        <label for="email">Email</label>
                    </div>
                    <div class="input-box">
                        <span class="icon-input"><i class='bx bxs-lock-alt' ></i></span>
                        <input type="password" name="password" id="password" required="required" autocomplete="off">
                        <label>Password</label>
                    </div>
                    <div class="remember-forgot">
                        <label><input type="checkbox">Remember me</label>
                        <a href="#">Forgot password?</a>
                    </div>
                    <button type="submit" class="btn" id="btn-in">Sign In</button>

                    <div class="login-register">
                        <p>Don't have an account?
                            <a href="./inscription.php" class="register-link">Sign up</a>
                        </p>
                    </div>
                </form>
            </div>
        </div>
    </div>
    
    
    <script src="js/header.js"></script>
    <script src="js/login.js"></script>
</body>
</html>