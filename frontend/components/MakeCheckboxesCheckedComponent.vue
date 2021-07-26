<template>
  <div>
    <!-- <v-app> -->
    <v-checkbox
      ref="projectTypeCheckboxes"
      @change="sendValueToParent(propsProjectTypes)"
      :input-value="propsProjectTypes"
      v-model="checked"
      :label="propsProjectTypes"
    ></v-checkbox>

    <!-- </v-app> -->
  </div>
</template>
<script>
export default {
  props: [
    "checked",
    "propsProjectTypes",
    "arrayOfProjectTypes",
    "allProjectTypes"
  ],
  methods: {
    sendValueToParent(value) {
      console.log(this.allProjectTypes, "value");
      if (this.allProjectTypes.indexOf(value) > -1) {
        console.log(this.arrayOfProjectTypes, value, "Checked Already");
        const projectInterests = this.arrayOfProjectTypes.includes(value)
          ? this.arrayOfProjectTypes.filter(item => item !== value)
          : [...this.arrayOfProjectTypes, value];
        console.log(this.arrayOfProjectTypes, value, "Not Checked Already");

        this.$emit("update:arrayOfProjectTypes", projectInterests);
      } else {
        console.log("eles");
      }
    }
  }
};
</script>