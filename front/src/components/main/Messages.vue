<template>
  <v-container>
    {% for message in get_flashed_messages() %}
    <v-alert type="info">
      { message }
    </v-alert>
    {% endfor %}
  </v-container>
</template>
