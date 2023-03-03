export type SportObject = {
  id: number
  latitude: number
  longitude: number
  is_active: boolean
}

export type SportObjectInfo = {
  name: string
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
}
