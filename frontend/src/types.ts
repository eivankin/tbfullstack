export type SportObject = {
  id: number
  latitude: number
  longitude: number
  is_active: boolean
  sport_types: { id: number; name: string }[]
}

export type SportObjectInfo = {
  name: string | null
  short_description: string | null
  full_description: string | null
  address: string | null
}

export type Choice = {
  id?: number
  name: string
}

export type FormRef = {
  fedEntity: Choice
  district: Choice
  locality: Choice
  sportType: Choice
  sportObjectType: Choice
}

export type MapRef = {
  getSportObjects: (
    fedEntityId: number | undefined,
    districtId: number | undefined,
    localityId: number | undefined,
    sportTypeId: number | undefined,
    sportObjectTypeId: number | undefined
  ) => void
  sportObjects: SportObject[]
  activityData: number[]
}
