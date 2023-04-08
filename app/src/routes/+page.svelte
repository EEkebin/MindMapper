<body>
	<div class="container">
		<h1>Mind Mapper</h1>
		<button on:click={() => window.location.href = "/login"}>Login</button>
	</div>
</body>

<head>
	<title>Mind Mapper</title>
	<style>
		body {
			margin: 0;
			padding: 0;
			background-color: #f1f1f1;
		}

		.container {
			width: 100%;
			max-width: 800px;
			margin: 0 auto;
			padding: 100px 20px;
			text-align: center;
		}

		h1 {
			font-size: 5rem;
			font-weight: bold;
			color: #333;
			margin-bottom: 20px;
		}

		button {
			padding: 12px 24px;
			border: none;
			border-radius: 4px;
			background-color: #007bff;
			color: #fff;
			font-size: 1.5rem;
			font-weight: bold;
			cursor: pointer;
		}

		button:hover {
			background-color: #0069d9;
		}
	</style>
</head>


