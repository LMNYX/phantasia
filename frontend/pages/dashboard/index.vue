<template>
  <div class="central-content">
    <div class="internal-navbar">
      <h1>Dashboard</h1>
      <div class="splitter"></div>
      <NuxtLink to="#" :class="{ active: currentInternalPage == 'overview' }">overview</NuxtLink>
      <NuxtLink to="/dashboard/uploads" :class="{ active: currentInternalPage == 'uploads' }">uploads</NuxtLink>
      <NuxtLink to="/dashboard/admin" :class="{ active: currentInternalPage == 'admin' }">admin</NuxtLink>
      <NuxtLink to="#" @click.prevent="handleLogout"><Icon name="material-symbols:logout" /></NuxtLink>
    </div>
    <div class="dashboard-page-content">
      <h2>Welcome back, {{ authStore.session?.username || 'User' }}!</h2>
      <div class="flex-block">
        <div id="upload-button" class="card" style="flex: 0 0 calc(33.333% - 0.5rem);" @click="triggerFileUpload">
          <input type="file" ref="fileInput" style="display: none" @change="handleFileUpload" />
          <button class="big-upload-button">
            <Icon name="solar:upload-broken" />
            <span class="sub-text">Upload a file</span>
          </button>
        </div>
        <div style="flex: 1;">
          <div class="just-a-block">
            <div class="card">
              <div class="header">
                <p>Your statistics</p>
                <div class="delimiter"></div>
              </div>
              <AreaChart
                :data="AreaChartData"
                :height="220"
                :categories="categories"
                :y-grid-line="true"
                :x-formatter="xFormatter"
                :x-num-ticks="4"
                :y-num-ticks="4"
                :curve-type="CurveType.MonotoneX"
                :legend-position="LegendPosition.Top"
              />
            </div>
            </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { useApiUrl } from '@/composables/useApiUrl'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
const router = useRouter()
const currentInternalPage = ref('overview')
const fileInput = ref<HTMLInputElement | null>(null)

console.log(authStore.session?.permissions);

const triggerFileUpload = () => {
  fileInput.value?.click()
}

const handleLogout = () => {
  authStore.logout()
  router.push('/')
}

const handleFileUpload = async (event: Event) => {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  if (!file) return

  const formData = new FormData()
  formData.append('file', file)

  const { apiBase } = useApiUrl()
  try {
    const response = await $fetch(`${apiBase}/uploads/create`, {
      method: 'POST',
      body: formData,
      headers: {
        'Authorization': `Token ${authStore.accessKey}`
      }
    })
    console.log('Upload successful:', response)
    alert('Upload successful!')
  } catch (error) {
    console.error('Upload failed:', error)
    alert('Upload failed. Check console for details.')
  } finally {
    // Reset the input value so the same file can be uploaded again if needed
    target.value = ''
  }
}

// chart
interface AreaChartItem {
  date: string
  Requests: number
  ['Errors']: number
}

const categories: Record<string, BulletLegendItemInterface> = {
  Requests: { name: 'Uploads', color: '#4B6A88' },
  Errors: { name: 'Views', color: '#fb2c36' },
}

const AreaChartData: AreaChartItem[] = [
  {
    date: 'Aug 01',
    Requests: 1040,
    Errors: 0,
  },
  {
    date: 'Aug 02',
    Requests: 1200,
    Errors: 0,
  },
  {
    date: 'Aug 03',
    Requests: 1130,
    Errors: 0,
  },
  {
    date: 'Aug 04',
    Requests: 1050,
    Errors: 0,
  },
  {
    date: 'Aug 05',
    Requests: 920,
    Errors: 0,
  },
  {
    date: 'Aug 06',
    Requests: 870,
    Errors: 0,
  },
  {
    date: 'Aug 07',
    Requests: 790,
    Errors: 0,
  },
  {
    date: 'Aug 08',
    Requests: 910,
    Errors: 0,
  },
  {
    date: 'Aug 09',
    Requests: 951,
    Errors: 0,
  },
  {
    date: 'Aug 10',
    Requests: 1232,
    Errors: 0,
  },
  {
    date: 'Aug 11',
    Requests: 1230,
    Errors: 0,
  },
  {
    date: 'Aug 12',
    Requests: 1289,
    Errors: 0,
  },
  {
    date: 'Aug 13',
    Requests: 1002,
    Errors: 0,
  },
  {
    date: 'Aug 14',
    Requests: 1034,
    Errors: 0,
  },
  {
    date: 'Aug 15',
    Requests: 1140,
    Errors: 0,
  },
  {
    date: 'Aug 16',
    Requests: 1280,
    Errors: 0,
  },
  {
    date: 'Aug 17',
    Requests: 1345,
    Errors: 0,
  },
  {
    date: 'Aug 18',
    Requests: 1432,
    Errors: 0,
  },
  {
    date: 'Aug 19',
    Requests: 1321,
    Errors: 0,
  },
  {
    date: 'Aug 20',
    Requests: 1230,
    Errors: 0,
  },
  {
    date: 'Aug 21',
    Requests: 1020,
    Errors: 0,
  },
  {
    date: 'Aug 22',
    Requests: 1040,
    Errors: 0,
  },
  {
    date: 'Aug 23',
    Requests: 610,
    Errors: 81,
  },
  {
    date: 'Aug 24',
    Requests: 610,
    Errors: 87,
  },
  {
    date: 'Aug 25',
    Requests: 610,
    Errors: 92,
  },
  {
    date: 'Aug 26',
    Requests: 501,
    Errors: 120,
  },
  {
    date: 'Aug 27',
    Requests: 480,
    Errors: 120,
  },
  {
    date: 'Aug 28',
    Requests: 471,
    Errors: 120,
  },
  {
    date: 'Aug 29',
    Requests: 610,
    Errors: 89,
  },
  {
    date: 'Aug 30',
    Requests: 513,
    Errors: 199,
  },
  {
    date: 'Aug 31',
    Requests: 500,
    Errors: 56,
  },
]
const xFormatter = (i: number): string | number => `${AreaChartData[i]?.date}`
const sum = (arr, key) => arr.reduce((sum, obj) => sum + obj[key], 0)
</script>

<style scoped lang="scss">
@use "@/assets/css/colors" as *;
.internal-navbar
{
  width: 100%;
  vertical-align: middle;

  h1
  {
    display: inline-block;
    vertical-align: middle;
  }

  div.splitter
  {
    display: inline-block;
    vertical-align: middle;
    width: 1px;
    height: 16px;
    background: rgba(255,255,255,0.15);
    margin: 0 16px;
  }

  a
  {
    display: inline-block;
    vertical-align: middle;
    margin: 0 4px;
    padding: 4px 8px;
    text-decoration: none;
    color: rgba(255,255,255,0.6);
    font-weight: 600;

    span
    {
      color: rgba(255,255,255,0.6);
      vertical-align: middle;
    }

    &:hover, &.active
    {
      color: $background-color;
      background-color: $highlight-color;

      span
      {
        color: $background-color;
      }
    }
  }
}

.big-upload-button
{
  width: 100%;
  height: 100%;
  background: transparent;
  border: none;
  outline: none;
  cursor: pointer;
  font-size: 32px;

  span.sub-text
  {
    display: block;
    font-size: 18px;
  }

  span
  {
    color: rgba(255,255,255,0.65);
  }

  &:hover
  {
    span
    {
      color: rgba(255,255,255,1);
    }
  }
}
</style>