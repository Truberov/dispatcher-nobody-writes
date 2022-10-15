import { create } from 'axios'

const timeout = 600000
const axiosInstance = create({ baseURL: 'http://127.0.0.1:8000/api/', timeout })
const defaultErrorInterceptor = (error) => Promise.reject(error)
const defaultRequestInterceptor = (config) => config
const defaultResponseInterceptor = (response) => response

export function setHeader(key, value) {
    axiosInstance.defaults.headers.common[key] = value
}

export function unsetHeader(key) {
    delete axiosInstance.defaults.headers.common[key]
}

export function addRequestInterceptor({ request, error }) {
    const interceptor = axiosInstance.interceptors.request.use(
        request || defaultRequestInterceptor,
        error || defaultErrorInterceptor
    )

    return () => {
        axiosInstance.interceptors.request.eject(interceptor)
    }
}

export function addResponseInterceptor({ response, error }) {
    const interceptor = axiosInstance.interceptors.response.use(
        response || defaultResponseInterceptor,
        error || defaultErrorInterceptor
    )

    return () => {
        axiosInstance.interceptors.response.eject(interceptor)
    }
}

const getAPI = {
    get: axiosInstance.get,
    delete: axiosInstance.delete,
    post: axiosInstance.post,
    put: axiosInstance.put,
    patch: axiosInstance.patch,
    request: axiosInstance.request
}

export default getAPI