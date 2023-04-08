<script>
    let username = "";
    let password = "";
    let confirmPassword = "";
    async function handleSubmit(event) {
        event.preventDefault();
        if (password !== document.getElementById("confirm-password").value) {
            alert("Passwords do not match.");
            return;
        }
        const response = await fetch(
            `http://localhost:5000/api/create_user/${username}/${password}`,
            {
                method: "POST",
            }
        );
        const status = await response.status;
        if (status === 200) {
            window.location.href = "/landingPage";
        } else {
            alert(
                "Registration failed. User either already exists, or passwords do not match."
            );
        }
    }
</script>

<head>
    <title>Placeholder Title</title>
</head>
<body>
    <div class="container">
        <h1>Register</h1>
        <form on:submit={handleSubmit}>
            <label for="username">Username:</label>
            <input
                type="text"
                id="username"
                name="username"
                placeholder="Enter your username"
                required
                bind:value={username}
            />
            <label for="password">Password:</label>
            <input
                type="password"
                id="password"
                name="password"
                placeholder="Enter your password"
                required
                bind:value={password}
            />
            <label for="confirm-password">Confirm Password:</label>
            <input
                type="password"
                id="confirm-password"
                name="confirm-password"
                placeholder="Confirm your password"
                required
                bind:value={confirmPassword}
            />
            <input type="submit" value="Register" />
        </form>
        <div class="create-account">
            Already have an account? <a href="/login">Login</a>.
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
    .error-message {
        color: red;
        font-size: 14px;
        margin-top: 10px;
    }
</style>
