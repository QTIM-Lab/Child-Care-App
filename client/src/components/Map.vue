<template>
    <div class=container>
            <div id="floating-panel">
                <input id="address" type="textbox" value="3318 Piney Forest Dr., Houston, TX 77084">
                <button @click="updateMap" id="submit">Find a Location</button>
            </div>
            <div id="map"></div>
    </div>
</template>

<script>
import gmapsInit from '../utils/gmaps';

export default {
  name: 'RequestMap',
  data() {
    return {
      google: '',
      geocoder: '',
      map: '',
    };
  },
  props: ['requests'],
  async mounted() {
    this.google = await gmapsInit();
    // console.log(AM_I_AVAILABLE);
    this.geocoder = new this.google.maps.Geocoder();
    // Init Map
    this.map = new this.google.maps.Map(document.getElementById('map'), {
      zoom: 12,
      center: { lat: 42.3601, lng: -71.0589 },
    });
    this.updateMap();
  },
  methods: {
    geocodeAddress(request) {
      // const street = document.getElementById('address').value;
      const street = request.address;
      this.geocoder.geocode({ address: street }, (results, status) => {
        if (status === 'OK') {
          const [result] = results;
          const { lat, lng } = result.geometry.location;
          return { lat, lng };
        }
        return { lat: -1, lng: -1 };
        // alert(`Geocode was not successful for the following reason: ${status}`);
      });
    },
    updateMap() {
      this.requests.forEach((request) => {
        // this.geocodeAddress(request);
        this.map.setCenter({ lat: 42.3601, lng: -71.0589 });
        this.map.setZoom(12);
        // Info window content
        const contentString = request.name;
        // Add info window
        const infowindow = new this.google.maps.InfoWindow({
          content: contentString,
          maxWidth: 200,
        });
        // Adding markers
        const marker = new this.google.maps.Marker({
          map: this.map,
          position: { lat: request.lat, lng: request.long },
        });
        marker.addListener('click', () => {
          infowindow.open(this.map, marker);
        });
      });
    },
    test() {
      return { lat: 5, long: 5 };
    },
  },
};
</script>

<style scoped>
    /* Always set the map height explicitly to define the size of the div
    * element that contains the map. */
    .container {
        height: 800px;
        width: 1000px;
    }
    #map {
    height: 100%;
    }
    /* Optional: Makes the sample page fill the window. */
    html, body {
    height: 100%;
    margin: 0;
    padding: 0;
    }
    #floating-panel {
    position: absolute;
    top: 10px;
    left: 25%;
    z-index: 5;
    background-color: #fff;
    padding: 5px;
    border: 1px solid #999;
    text-align: center;
    font-family: 'Roboto','sans-serif';
    line-height: 30px;
    padding-left: 10px;
    }
</style>
