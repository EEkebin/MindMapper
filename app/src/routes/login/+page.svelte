<script>
    let username = "";
    let password = "";
    async function handleSubmit(event) {
        event.preventDefault();
        const response = await fetch(
            `http://localhost:5000/api/login_user/${username}/${password}`,
            {
                method: "GET",
            }
        );
        const status = await response.status;
        if (status === 200) {
            window.addEventListener("beforeunload", (event) => {
                localStorage.setItem("username", username);
                localStorage.setItem("password", password);
            });
            window.location.href = "/landingPage";
        } else {
            alert("Login failed. Please check your username and password.");
        }
    }
</script>

<head>
    <title>Placeholder Title</title>
</head>
<body>
    <div class="container">
        <h1>Login</h1>
        <form on:submit={handleSubmit}>
            <label for="username">Username:</label>
            <input
                type="text"
                id="username"
                name="username"
                placeholder="Enter your username"
                bind:value={username}
            />
            <label for="password">Password:</label>
            <input
                type="password"
                id="password"
                name="password"
                placeholder="Enter your password"
                bind:value={password}
            />
            <input type="submit" value="Login" />
        </form>
        <div class="create-account">
            Don't have an account? <a href="/register">Create one</a>.
        </div>
    </div>
</body>

<style>
    body {
        background-color: #f2f2f2;
        font-family: Arial, sans-serif;
    }
    .container {
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0px 0px 10px #ccc;
        margin: 100px auto;
        max-width: 400px;
        padding: 20px;
    }
    h1 {
        text-align: center;
    }
    input[type="text"],
    input[type="password"] {
        border: none;
        border-bottom: 2px solid #ccc;
        font-size: 16px;
        margin-bottom: 20px;
        padding: 10px;
        width: 95%;
    }
    input[type="submit"] {
        background-color: #007bff;
        border: none;
        border-radius: 5px;
        color: #fff;
        cursor: pointer;
        font-size: 16px;
        padding: 10px;
        width: 95%;
    }
    input[type="submit"]:hover {
        background-color: #0069d9;
    }
    .create-account {
        display: block;
        margin-top: 20px;
        text-align: center;
    }
    .create-account a {
        color: #007bff;
        text-decoration: none;
    }
    .create-account a:hover {
        text-decoration: underline;
    }
</style>
