<template>
  <div>
    <div class="row">
      <div class="col-sm-10">
        <h1>Help Requests</h1>
        <p>Please use this requests system to add availability
          to help others or if you yourself need assistance.</p>
        <hr>
        <p><i>Refresh browser to see changes reflected on map.</i></p>
        <br>
        <!-- <rmap v-bind:requests="requests" ref="ourmap" v-on:></rmap> -->
        <div class=container>
                <!-- <div id="floating-panel">
                    <button @click="updateMap" id="submit">Refresh Map</button>
                </div> -->
                <div id="map"></div>
        </div>
        <br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button"
                class="btn btn-success btn-sm"
                v-b-modal.request-modal>Add Request
        </button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Email</th>
              <th scope="col">Address</th>
              <th scope="col">Request/Service</th>
              <th scope="col">Need Help?</th>
              <th scope="col">Can Help?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(request, index) in requests" :key="index">
              <td>{{ request.name }}</td>
              <td>{{ request.email }}</td>
              <td>{{ request.address }}</td>
              <td>{{ request.request }}</td>
              <td>
                <span v-if="request.needHelp">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <span v-if="request.canHelp">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.request-update-modal
                          @click="editRequest(request)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteRequest(request)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addRequestModal"
            id="request-modal"
            request="Add a new request"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-name-group"
                      label="Name:"
                      label-for="form-name-input">
            <b-form-input id="form-name-input"
                          type="text"
                          v-model="addRequestForm.name"
                          required
                          placeholder="First Last">
            </b-form-input>
        </b-form-group>

        <b-form-group id="form-email-group"
                      label="Email:"
                      label-for="form-email-input">
            <b-form-input id="form-email-input"
                          type="text"
                          v-model="addRequestForm.email"
                          required
                          placeholder="username@gmail.com">
            </b-form-input>
        </b-form-group>

        <b-form-group id="form-address-group"
                      label="Address:"
                      label-for="form-address-input">
            <b-form-input id="form-address-input"
                          type="text"
                          v-model="addRequestForm.address"
                          required
                          placeholder="123 Pleasant St., Morgantown, WV 26505">
            </b-form-input>
        </b-form-group>

        <b-form-group id="form-request-group"
                    label="Request:"
                    label-for="form-request-input">
          <b-form-input id="form-request-input"
                        type="text"
                        v-model="addRequestForm.request"
                        required
                        placeholder="Enter request">
          </b-form-input>
        </b-form-group>

        <b-form-group id="form-needHelp-group">
          <b-form-checkbox-group v-model="addRequestForm.needHelp" id="form-checks">
            <b-form-checkbox value="true">Need Help?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>

        <b-form-group id="form-canHelp-group">
          <b-form-checkbox-group v-model="addRequestForm.canHelp" id="form-checks">
            <b-form-checkbox value="true">Can Help?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>

        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>

      </b-form>
    </b-modal>
    <b-modal ref="editRequestModal"
            id="request-update-modal"
            request="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">

        <b-form-group id="form-name-edit-group"
                      label="Name:"
                      label-for="form-name-edit-input">
            <b-form-input id="form-name-edit-input"
                          type="text"
                          v-model="editForm.name"
                          required
                          placeholder="First Last">
            </b-form-input>
        </b-form-group>

        <b-form-group id="form-email-edit-group"
                    label="Email:"
                    label-for="form-email-edit-input">
          <b-form-input id="form-email-edit-input"
                        type="text"
                        v-model="editForm.email"
                        required
                        placeholder="username@gmail.com">
          </b-form-input>
        </b-form-group>

        <b-form-group id="form-address-edit-group"
                    label="Address:"
                    label-for="form-address-edit-input">
          <b-form-input id="form-address-edit-input"
                        type="text"
                        v-model="editForm.address"
                        required
                        placeholder="123 Pleasant St., Morgantown WV 26505">
          </b-form-input>
        </b-form-group>

        <b-form-group id="form-request-edit-group"
                    label="Title:"
                    label-for="form-request-edit-input">
          <b-form-input id="form-request-edit-input"
                        type="text"
                        v-model="editForm.request"
                        required
                        placeholder="Enter request">
          </b-form-input>
        </b-form-group>

        <b-form-group id="form-needHelp-edit-group">
          <b-form-checkbox-group v-model="editForm.needHelp" id="form-checks">
            <b-form-checkbox value="true">need help?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>

        <b-form-group id="form-canHelp-edit-group">
          <b-form-checkbox-group v-model="editForm.canHelp" id="form-checks">
            <b-form-checkbox value="true">Can help?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>

        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
// import RequestMap from './Map.vue';
import gmapsInit from '../utils/gmaps';

export default {
  data() {
    return {
      lat: '',
      lng: '',
      google: '',
      geocoder: '',
      map: '',
      requests: [],
      addRequestForm: {
        name: '',
        email: '',
        address: '',
        request: '',
        needHelp: [],
        canHelp: [],
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        name: '',
        email: '',
        address: '',
        request: '',
        needHelp: [],
        canHelp: [],
      },
    };
  },
  async mounted() {
    this.google = await gmapsInit();
    this.geocoder = new this.google.maps.Geocoder();
    this.map = new this.google.maps.Map(document.getElementById('map'), {
      zoom: 12,
      center: { lat: 42.3601, lng: -71.0589 },
    });
    // this.updateMap(this.requests);
    this.updateMap();
  },
  components: {
    alert: Alert,
    // rmap: RequestMap,
  },
  methods: {
    getRequests() {
      const path = 'http://172.21.14.152:5000/requests';
      axios.get(path)
        .then((res) => {
          this.requests = res.data.requests;
          this.updateMap();
          // this.updateMap(this.requests);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addRequest(payload) { // actually posts data to db
      const path = 'http://172.21.14.152:5000/requests';
      axios.post(path, payload)
        .then(() => {
          this.getRequests();
          this.message = 'Request added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getRequests();
        });
    },
    initForm() {
      this.addRequestForm.name = '';
      this.addRequestForm.email = '';
      this.addRequestForm.address = '';
      this.addRequestForm.request = '';
      this.addRequestForm.needHelp = [];
      this.addRequestForm.canHelp = [];
      this.editForm.id = '';
      this.editForm.name = '';
      this.editForm.email = '';
      this.editForm.address = '';
      this.editForm.request = '';
      this.editForm.needHelp = [];
      this.editForm.canHelp = [];
    },
    geocodeAddress(request, fn) {
      // return { lat: 5, long: 5 };
      // const street = document.getElementById('address').value;
      const street = request.address;
      this.geocoder.geocode({ address: street }, (results) => {
        // console.log(typeof(this));
        // console.log(results[0].geometry.location.lat());
        // console.log(results[0].geometry.location.lng());
        const test = {
          lat: results[0].geometry.location.lat(),
          long: results[0].geometry.location.lng(),
        };
        // if (status === 'OK') {
        //   const [result] = results;
        //   const { lat, lng } = result.geometry.location;
        //   return { lat, lng };
        // }
        // return { lat: -1, lng: -1 };
        // alert(`Geocode was not successful for the following reason: ${status}`);
        fn(test);
      });
    },
    removeAllMarkers() {
      this.map.data.forEach((feature) => {
        if (feature.getGeometry().getType() === 'Point') {
          this.map.data.remove(feature);
        }
      });
    },
    updateMap() {
      this.removeAllMarkers();
      this.requests.forEach((request) => {
        // this.geocodeAddress(request);
        // this.map.setCenter({ lat: 42.3601, lng: -71.0589 });
        // this.map.setZoom(12);
        // Info window content
        const contentString = `<h3>${request.name}</h3><hr><br><p>${request.request}</p>`;
        // Add info window
        const infowindow = new this.google.maps.InfoWindow({
          content: contentString,
          maxWidth: 200,
        });
        // Adding markers
        const marker = new this.google.maps.Marker({
          map: this.map,
          position: { lat: request.lat, lng: request.long },
          icon: 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png',
        });
        marker.addListener('click', () => {
          infowindow.open(this.map, marker);
        });
      });
    },
    onSubmit(evt) { // when you click submit of new request form
      evt.preventDefault();
      this.$refs.addRequestModal.hide();
      let needHelp = false;
      if (this.addRequestForm.needHelp[0]) needHelp = true;
      let canHelp = false;
      if (this.addRequestForm.canHelp[0]) canHelp = true;
      this.geocodeAddress(this.addRequestForm, (test) => {
        const payload = {
          name: this.addRequestForm.name,
          email: this.addRequestForm.email,
          address: this.addRequestForm.address,
          lat: test.lat,
          long: test.long,
          request: this.addRequestForm.request,
          needHelp, // property shorthand
          canHelp,
        };
        this.addRequest(payload);
        this.initForm();
      });
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addRequestModal.hide();
      this.initForm();
    },
    editRequest(request) {
      this.editForm = request;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editRequestModal.hide();
      let needHelp = false;
      if (this.editForm.needHelp[0]) needHelp = true;
      let canHelp = false;
      if (this.editForm.canHelp[0]) canHelp = true;
      this.geocodeAddress(this.editForm, (test) => {
        const payload = {
          name: this.editForm.name,
          email: this.editForm.email,
          address: this.editForm.address,
          lat: test.lat,
          long: test.long,
          request: this.editForm.request,
          needHelp, // property shorthand
          canHelp,
        };
        this.updateRequest(payload, this.editForm.id);
      });
      // const payload = {
      //   name: this.editForm.name,
      //   email: this.editForm.email,
      //   address: this.editForm.address,
      //   request: this.editForm.request,
      //   needHelp,
      //   canHelp,
      // };
      // this.updateRequest(payload, this.editForm.id);
    },
    updateRequest(payload, requestID) {
      const path = `http://172.21.14.152:5000/requests/${requestID}`;
      axios.put(path, payload)
        .then(() => {
          this.getRequests();
          this.message = 'Request updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getRequests();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editRequestModal.hide();
      this.initForm();
      this.getRequests(); // why?
    },
    removeRequest(requestID) {
      const path = `http://172.21.14.152:5000/requests/${requestID}`;
      axios.delete(path)
        .then(() => {
          this.getRequests();
          this.message = 'Request removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getRequests();
        });
    },
    onDeleteRequest(request) {
      this.removeRequest(request.id);
    },
  },
  created() {
    this.getRequests();
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
