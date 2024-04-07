import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import {
  Route,
  RouterProvider,
  createBrowserRouter,
  createRoutesFromElements,
} from "react-router-dom";

import MainPage from "./component/MainPage/MainPage.jsx";
import RepositoryPage from "./component/RepositoryPage/RepositoryPage.jsx";
import ContentPage from "./component/ContentPage/ContentPage.jsx";
import AllContextProvider from "./context/AllContextProvider.jsx";
import Functionality from "./component/Functionality/Functionality.jsx";

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="" element={<Functionality />}>
      <Route path="repositories" element={<RepositoryPage />}/>
    </Route>
  )
);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <AllContextProvider>
    <div className="ParentContainer">
      <RouterProvider router={router} />
    </div>
    </AllContextProvider>
  </React.StrictMode>
);