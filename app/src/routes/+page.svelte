<script>
  let username = "";
  let password = "";
  async function handleSubmit(event) {
    event.preventDefault();
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
      alert("Registration failed. Please check your username and password.");
    }
  }
</script>

<form on:submit={handleSubmit}>
  <input type="text" bind:value={username} placeholder="Username" />
  <input type="password" bind:value={password} placeholder="Password" />
  <button type="submit">Register</button>
</form>
