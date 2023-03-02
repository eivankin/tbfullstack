/// <reference types="vite/client" />
interface ImportMetaEnv {
  readonly VITE_MAPBOX_API_KEY: string,
  readonly VITE_API_ENDPOINT: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
