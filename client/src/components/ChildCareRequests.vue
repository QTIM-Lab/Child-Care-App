<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Live Child Care Requests</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button"
                class="btn btn-success btn-sm"
                v-b-modal.request-modal>Add Request</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Request/Service</th>
              <th scope="col">Parent/Guardian</th>
              <th scope="col">Need Help?</th>
              <th scope="col">Can Help?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(request, index) in requests" :key="index">
              <td>{{ request.request }}</td>
              <td>{{ request.parentGuardian }}</td>
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

        <b-form-group id="form-parentGuardian-group"
                      label="Parent/Guardian:"
                      label-for="form-parentGuardian-input">
            <b-form-input id="form-parentGuardian-input"
                          type="text"
                          v-model="addRequestForm.parentGuardian"
                          required
                          placeholder="Enter parentGuardian">
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

        <b-form-group id="form-parentGuardian-edit-group"
                      label="Author:"
                      label-for="form-parentGuardian-edit-input">
            <b-form-input id="form-parentGuardian-edit-input"
                          type="text"
                          v-model="editForm.parentGuardian"
                          required
                          placeholder="Enter parentGuardian">
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

export default {
  data() {
    return {
      requests: [],
      addRequestForm: {
        request: '',
        parentGuardian: '',
        needHelp: [],
        canHelp: [],
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        request: '',
        parentGuardian: '',
        needHelp: [],
        canHelp: [],
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getRequests() {
      const path = 'http://172.21.14.152:5000/requests';
      axios.get(path)
        .then((res) => {
          this.requests = res.data.requests;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addRequest(payload) {
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
      this.addRequestForm.request = '';
      this.addRequestForm.parentGuardian = '';
      this.addRequestForm.needHelp = [];
      this.addRequestForm.canHelp = [];
      this.editForm.id = '';
      this.editForm.request = '';
      this.editForm.parentGuardian = '';
      this.editForm.needHelp = [];
      this.editForm.canHelp = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addRequestModal.hide();
      let needHelp = false;
      if (this.addRequestForm.needHelp[0]) needHelp = true;
      let canHelp = false;
      if (this.addRequestForm.canHelp[0]) canHelp = true;
      const payload = {
        request: this.addRequestForm.request,
        parentGuardian: this.addRequestForm.parentGuardian,
        needHelp, // property shorthand
        canHelp,
      };
      this.addRequest(payload);
      this.initForm();
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
      const payload = {
        request: this.editForm.request,
        parentGuardian: this.editForm.parentGuardian,
        needHelp,
        canHelp,
      };
      this.updateRequest(payload, this.editForm.id);
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
