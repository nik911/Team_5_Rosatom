<script>
  import Router from "svelte-spa-router";
  import NewVessel from "./pages/NewVessel.svelte";
  import NewApplication from "./pages/NewApplication.svelte";
  import WeatherReport from "./pages/WeatherReport.svelte";
  import Map from "./pages/Map.svelte";
  import Chart from "./pages/Chart.svelte";

  const routes = {
    "/vessel": NewVessel,
    "/application": NewApplication,
    "/weather": WeatherReport,
    "/chart": Chart,
    "/": Map,
  };
</script>

<Router {routes} />
