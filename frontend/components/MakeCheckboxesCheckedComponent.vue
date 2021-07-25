<template>
  <div>
    <v-app>
      <!-- <input
        type="checkbox"
        ref="projectTypeCheckboxes"
        @change="sendValueToParent(propsProjectTypes)"
        :value="propsProjectTypes"
        :checked="checked"
      />-->
      <v-checkbox
        ref="projectTypeCheckboxes"
        @change="sendValueToParent(propsProjectTypes)"
        :value="propsProjectTypes"
        :checked="checked"
        v-model="checked"
      ></v-checkbox>
      {{propsProjectTypes}} {{checked}}
    </v-app>
  </div>
</template>
<script>
export default {
  props: ["checked", "propsProjectTypes", "arrayOfProjectTypes"],
  methods: {
    sendValueToParent(value) {
      if (
        // [
        //   "AC",
        //   "AD",
        //   "Boom Operator",
        //   "Composer",
        //   "Costume Design",
        //   "DP",
        //   "UPM",
        //   "Gaffer",
        //   "Grip",
        //   "HMU",
        //   "PA",
        //   "Pass Van Driver",
        //   "Set Photographer",
        //   "Producer",
        //   "Production Designer",
        //   "Set Design",
        //   "Sound Wrangler",
        //   "Script Supervising"
        // ]
        this.arrayOfProjectTypes.indexOf(value) > -1
      ) {
        console.log(this.arrayOfProjectTypes, value, "ARRAY CREW POS");
        const projectInterests = this.arrayOfProjectTypes.includes(value)
          ? this.arrayOfProjectTypes.filter(item => item !== value)
          : [...this.arrayOfProjectTypes, crew];
        this.$emit("update:arrayOfProjectTypes", projectInterests);
      }
      //   else if (
      //     [
      //       "Editing",
      //       "Sound Mixer",
      //       "Music Composer",
      //       "Audio Engineer",
      //       "Sound Editor",
      //       "Producer"
      //     ].indexOf(crew) > -1
      //   ) {
      //     console.log(this.arrayPostPositions, crew, "ARRAY POST POS");
      //     const positions = this.arrayPostPositions.includes(crew)
      //       ? this.arrayPostPositions.filter(item => item !== crew)
      //       : [...this.arrayPostPositions, crew];
      //     this.$emit("update:arrayPostPositions", positions);
      //   }
    }
  }
};
</script>