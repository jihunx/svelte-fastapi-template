<script>
    let inputNumber;
    let answer;

    let getBackendData = async (endpoint) => {
        let response = await fetch(`http://0.0.0.0:8000/api${endpoint}`);
        let result = await response.json();
        if (response.ok) {
            return result;
        } else {
            throw new Error(result);
        }
    }

    let getSquare = async (inputNumber) => {
        let result = await getBackendData(`/get_square/${inputNumber}`);
        answer = result.answer;
    }

</script>

<main>
    <input type="text" bind:value={inputNumber}>
    <button on:click={getSquare(inputNumber)}>Get Square</button>
    {#await getBackendData}
        <div class="spinner">Loading...</div>
    {:then result}
        <div class="">Square: {answer || "Input number above"}</div>
    {:catch error}
        <div class="uppercase text-red-700">{error.message}</div>
    {/await}
</main>