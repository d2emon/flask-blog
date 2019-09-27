<template>
  <base-widget
    title="Tags"
  >
    <div class="tagcloud">
      <a
        v-for="(tag, tagId) in tags"
        :key="`tag-${tag.tagId}`"
        class="tag-link-17"
        :style="`${colorClass[tagId]}${rowClass[tagId]}`"
        :href="`/tag/${tag.tagId}`"
      >
        {{ tag.name }}
      </a>

    </div>
  </base-widget>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {
  mapState,
} from 'vuex';

@Component({
  components: {
    BaseWidget: () => import('@/components/widgets/BaseWidget.vue'),
  },
})
export default class Tags extends Vue {
  tags = [
    { tagId: 1, name: 'Tag1' },
    { tagId: 2, name: 'Tag2' },
    { tagId: 3, name: 'Tag3' },
    { tagId: 4, name: 'Tag4' },
    { tagId: 5, name: 'Tag5' },
  ];

  rowClass = [
    'font-size:12.656565656pt;',
    'font-size:8pt;',
    'font-size:21.0567465745647pt;',
    'font-size:9.0567465745647pt;',
    'font-size:7.0567465745647pt;',
    'font-size:14.0567465745647pt;',
    'font-size:17.0567465745647pt;',
    'font-size:10.0567465745647pt;',
    'font-size:18.0567465745647pt;',
    'font-size:9.0567465745647pt;',
    'font-size:16.0567465745647pt;',
    'font-size:19.0567465745647pt;',
    'font-size:7.0567465745647pt;',
    'font-size:10.0567465745647pt;',
    'font-size:15.0567465745647pt;',
    'font-size:8.0567465745647pt;',
    'font-size:20.0567465745647pt;',
    'font-size:17.0567465745647pt;',
    'font-size:14.0567465745647pt;',
    'font-size:15.0567465745647pt;',
  ];

  colorClass = [
    'color:#ac1dfe;',
    'color:#bcb46e;',
    'color:#4298e7;',
    'color:#a7bce8',
    'color:#e6eca8;',
    'color:#d4349a;',
    'color:#5b48ce;',
    'color:#b5b1ea;',
    'color:#fe4516;',
    'color:#a68d32;',
    'color:#68d6e5;',
    'color:#5c8d29;',
    'color:#9c7da1;',
    'color:#243f2a;',
    'color:#6c7d99;',
    'color:#9cade9;',
    'color:#1ced29;',
    'color:#ec3de9;',
    'color:#367d29;',
    'color:#cccd29;',
  ];
}
</script>
