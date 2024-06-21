const LoginPage = () => {

    return (
        <div className="flex justify-center items-center h-screen bg-blue-500">
            <div className="bg-white p-8 rounded shadow">
                <h1 className="text-2xl font-bold mb-4">Login</h1>
                <input type="text" placeholder="Username" className="w-full border border-gray-300 rounded px-3 py-2 mb-4" />
                <input type="password" placeholder="Password" className="w-full border border-gray-300 rounded px-3 py-2 mb-4" />
                <button className="bg-blue-500 text-white rounded px-4 py-2">Login</button>
            </div>
        </div>
    );
}
export default LoginPage