import { configureStore } from "@reduxjs/toolkit";
import taskReducer from './Counter'

export default configureStore({
    reducer: {
        task: taskReducer
    }
})