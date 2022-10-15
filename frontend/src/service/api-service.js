import getAPI from './axios-base'

const apiClient = {
    async getTransport() {
        const response = await getAPI.get('/transport/')

        return response.data
    },
}
export default apiClient
