<script>
  let info = {
    names: ["Штурман Кошелев", "Лагорта", "Юрий Кучиев"],
    points: ["Саббета 1", "Саббета 2", "Саббета 3", "Точка в Баренцевом море"],
  };

  let data = {};

  $: console.log(data);
</script>

<main>
  <div class="container">
    <header>
      <h1>Новая заявка</h1>
    </header>
    <label>Судно</label>
    <select required bind:value={data.name}>
      {#each info.names as vessel}
        <option>{vessel}</option>
      {/each}
    </select>
    <fieldset class="grid">
      <div>
        <label>Пункт начала плавания</label>
        <select required bind:value={data.startPoint}>
          {#each info.points as point}
            <option>{point}</option>
          {/each}
        </select>
      </div>
      <div>
        <label>Пункт окончания плавания</label>
        <select required bind:value={data.endPoint}>
          {#each info.points as point}
            <option>{point}</option>
          {/each}
        </select>
      </div>
    </fieldset>
    <fieldset class="grid">
      <div>
        <label>Дата и время начала плавания</label>
        <input type="datetime-local" bind:value={data.startTime} />
      </div>
      <div>
        <label>Дата и время окончания плавания</label>
        <input type="datetime-local" bind:value={data.endTime} />
      </div>
    </fieldset>
    <button>Отправить заявку</button>
  </div>
</main>
