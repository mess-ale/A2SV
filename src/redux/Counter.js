import { createSlice } from "@reduxjs/toolkit";

export const counterSlice = createSlice({
  name: 'tasker',
  initialState: {
    count: 0,
  },
  reducers: {
    adding: (state) => {
      state.count += 1
    },
    updating: (stata, value) => {
      stata.count = value.payload
    },
    removing: (state) => {
      state.count = state.count
    }
  }
})

export const { adding, updating, removing } = counterSlice.actions
export default counterSlice.reducer;